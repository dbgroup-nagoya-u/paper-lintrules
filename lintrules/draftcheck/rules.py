"""This module contains rule definitions."""

#####################################################################
# This file was forked from https://github.com/ebnn/draftcheck.
# That project would be MIT LICENSE since some URL show its LICENSE.
# See https://libraries.io/pypi/draftcheck
# See also https://pypi.org/project/draftcheck/
#####################################################################

import re

# Global rules list to store all the registered rules
RULES_LIST = []

def rule(pattern, show_spaces=False, in_env="paragraph"):
    """Decorator used to create rules.

    The decorated function must have the following signature:
        def example_rule(text, matches):
            return ...

    where `text` is the string that needs to be checked, and matches is the
    result of calling `re.finditer(pattern, text)`, i.e. the `MatchObject`s
    representing substrings that match the specified regex pattern.

    The decorated function must return a list of tuple pairs, where each tuple
    pair (start, end) represents the start and end indices of substrings in
    `text` that violate the rule.

    Parameters
    ----------
    pattern : string
        If specified, pattern is treated as a regular expression and the result
        of calling `finditer` on the text being checked is passed to the wrapped
        function.
    show_spaces : boolean, optional
        Whether the output should replace whitespace with underscores
        (in order to clearly indicate errors involving whitespace). Defaults to
        false.
    in_env : string, optional
        The LaTeX environment in which this rule can be applied. Only text in
        the specified environment are checked against this rule. This may be
        set to 'any' if this rule applies in any environment. Defaults to
        'paragraph'.
    """
    regexpr = re.compile(pattern)

    def inner_rule(func):
        def wrapper(text, env):
            if in_env == "any" or env == in_env:
                return func(text, regexpr.finditer(text))
            return []

        # Store the parameters in the function as attributes
        wrapper.id = len(RULES_LIST) + 1
        wrapper.show_spaces = show_spaces
        wrapper.in_env = in_env

        # Inherit the docstring from the function
        wrapper.__doc__ = func.__doc__

        # Add it to our global rules list
        RULES_LIST.append(wrapper)

        return wrapper

    return inner_rule

def rule_generator(show_spaces=False, in_env="paragraph"):
    """Decorator that generates rules from a generator."""

    def inner_rule(func):
        for r in func():
            # Register this rule into our global rules list
            @rule(pattern=r[0], show_spaces=show_spaces, in_env=in_env)
            def generated_rule(_, matches):
                return [m.span() for m in matches]

            # Format the docstring with parameters specific to this instance
            # of the rule
            RULES_LIST[-1].__doc__ = func.__doc__.format(*r[1:])

    return inner_rule

@rule(r"\s+\\footnote(\[\d*\])?{", show_spaces=True)
def check_space_before_footnote(text, matches):
    """Do not precede footnotes with spaces.

    Remove the extraneous spaces before the \\footnote command.

    Examples
    --------
    Bad:
        Napolean's armies were defeated in Waterloo \\footnote{In present day
        Belgium}.

    Good:
        Napolean's armies were defeated in Waterloo\\footnote{In present day
        Belgium}.
    """
    return [m.span() for m in matches]

@rule(r"．~?\\cite{")
def check_cite_after_period(text, matches):
    r"""句点の前で引用をしてください．例：`~\cite{vldb2020:author}．`

    Move the \\cite command inside the sentence, before the period.

    Examples
    --------
    Bad:
        Johannes Brahms was born in Hamburg.\\cite{}

    Good:
        Johannes Brahms was born in Hamburg~\\cite{}.
    """
    return [m.span() for m in matches]

@rule(r"[^~]\\cite{")
def check_no_space_before_cite(text, matches):
    r"""行頭に引用がくるのを禁止するため，引用の前に`~`を追加してください．

    Examples
    --------
    Bad:
        Apollo 17's ``The Blue Marble'' \\cite{} photo of the Earth became an
        icon of the environmental movement.

    Good:
        Apollo 17's ``The Blue Marble''~\\cite{} photo of the Earth became an
        icon of the environmental movement.
    """
    return [m.span() for m in matches]

@rule(r"[^~{]\\ref{")
def check_no_space_before_ref(text, matches):
    r"""行頭に参照がくるのを禁止するため，`\ref`の前に`~`を追加してください．あるいは研究室のtexファイル中の`\newcommand`で定義されたコマンドを使用してください．

    Examples
    --------
    Bad:
        The performance of the engine is shown in Figure \\ref{}.

    Good:
        The performance of the engine is shown in Figure~\\ref{}.
    """
    return [m.span() for m in matches]

@rule(r"\d+%")
def check_unescaped_percentage(text, matches):
    r"""`%`を使用する場合は`\%`と書いてください．

    Examples
    --------
    Bad:
        The company's stocks rose by 15%.

    Good:
        The company's stocks rose by 15\\%.
    """
    return [m.span() for m in matches]

@rule(r"\d+\s?x\s?\d+")
def check_incorrect_usage_of_x_as_times(text, matches):
    r"""数値の間に`x`を入れたい場合は`\times`または`\multiply`を使用してください．

    Example
    -------
    Bad:
        We used an 10x10 grid for the image filter.

    Good:
        We used an $10 \\times 10$ grid for the image filter.
    """
    return [m.span() for m in matches]

@rule(r'([a-z]|[^\x01-\x7E])+\s-\s([a-z]|[^\x01-\x7E])+')
def check_space_surrounded_dash(text, matches):
    """`-`ではなく`---`を使用してください．

    Example
    -------
    Bad:
        He only desired one thing - success.

    Good:
        He only desired one thing --- success.
    """
    return [m.span() for m in matches]

@rule(r"(\.\.\.|…)")
def check_dot_dot_dot(text, matches):
    r"""`...`ではなく`\ldots`を使用してください．

    Example
    -------
    Bad:
        New York, Tokyo, Budapest, ...

    Good:
        New York, Tokyo, Budapest, \\ldots
    """
    return [m.span() for m in matches]

@rule(r'(?<!{\\)["”“″〝゛‶].+?["”“″〝゛‶]')
def check_double_quote(text, matches):
    r"""ダブルクオートで文字を囲わず``` ``文字'' ```としてください．

    Example
    -------
    Bad:
        "Very much indeed," Alice said politely.

    Good:
        ``Very much indeed,'' Alice said politely.
    """
    return [m.span() for m in matches]

@rule(r"['’′´‘＇][^`]+?['’′´‘＇]")
def check_single_quote(text, matches):
    r"""シングルクオートで文字を囲わず`` `文字' ``としてください．

    Example
    -------
    Bad:
        It is 'too good to be true'.

    Good:
        It is `too good to be true'.
    """
    return [m.span() for m in matches]

@rule(r"\\begin{center}", in_env="any")
def check_begin_center(text, matches):
    r"""`\begin{center}`ではなく`\centering`を使用してください．

    Example
    -------
    Bad:
        \\begin{figure}
            \\begin{center}
                \\includegraphics
            \\end{center}
        \\end{figure}

    Good:
        \\begin{figure}
            \\centering
            \\includegraphics
        \\end{figure}
    """
    return [m.span() for m in matches]

@rule(r"\$\$", in_env="math")
def check_double_dollar_math(text, matches):
    r"""数式は`$$`ではなく`\[`あるいは`\begin{equation}`を使用してください.

    Example
    -------
    Bad:
        $$ 1 + 1 = 2 $$

    Good:
        \\[ 1 + 1 = 2 \\]

    Good:
        \\begin{equation}
            1 + 1 = 2
        \\end{equation}
    """
    return [m.span() for m in matches]

@rule(r"\d\s?-\s?\d")
def check_numeric_range_dash(text, matches):
    r"""数値の範囲は`-`ではなく`--`を使用してください．

    Example
    -------
    Bad:
        A description of medical practices at the time are on pages 17-20.

    Good:
        A description of medical practices at the time are on pages 17--20.
    """
    return [m.span() for m in matches]

@rule(r"\\footnote{.+?}[,.]")
def check_footnote_before_punctuation(text, matches):
    r"""英文では`\footnote`を句読点の直後に配置してください．

    Example
    -------
    Bad:
        \\emph{Waiting for Godot}\\footnote{First performed on 5 January 1953 in
        Paris}, written by Samuel Beckett, is an example of Absurdist Theatre.

    Good:
        \\emph{Waiting for Godot},\\footnote{First performed on 5 January 1953 in
        Paris} written by Samuel Beckett, is an example of Absurdist Theatre.
    """
    return [m.span() for m in matches]

@rule(r"[，．]\\footnote{.+?}")
def check_footnote_before_punctuation(text, matches):
    r"""和文では`\footnote`を句読点の直前に配置してください．

    Example
    -------
    Bad:
        待機のためにスピンロックを使用する．footnote{アルゴリズムでは簡略化のため単にスピンロックと
        しているが，実際にはブロッキングを組み合わせ無駄なCPUコアの使用を抑制している．}

    Good:
        待機のためにスピンロックを使用するfootnote{アルゴリズムでは簡略化のため単にスピンロックと
        しているが，実際にはブロッキングを組み合わせ無駄なCPUコアの使用を抑制している．}．
    """
    return [m.span() for m in matches]

@rule(r"<[^\s](.+?)[^\s]>", in_env="math")
def check_relational_operators(text, matches):
    r"""大小関係を表さない`<>`は`\langle`と`\rangle`を使用してください．
    Example
    -------
    Bad:
        Inner product of $a$ and $b$ is denoted by $<a, b>$.

    Good:
        Inner product of $a$ and $b$ is denoted by $\\langle a, b \\rangle$.

    Good:
        It must satisfy this inequality: $a < b, c > d$.
    """
    return [m.span() for m in matches]

@rule(r"\\cite{.+?}[\s~，]*\\cite{")
def check_multiple_cite(text, matches):
    r"""一度に複数の参考文献を挙げる場合は`~\cite{..., ...}`としてください．

    Example
    -------
    Bad:
        This problem has many real-world applications~\\cite{A}\\cite{B}.

    Good:
        This problem has many real-world applications~\\cite{A, B}.
    """
    return [m.span() for m in matches]

@rule(r"\d[\s　]?(ms|s|A|cores?|GHz|heyperthreads?|bytes?|bit|KB|MB|GB|TB|PB)\b")
def check_number_next_to_unit(text, matches):
    r"""数値と単位の間には`~`を入れてください．例：`64~GB`

    Example
    -------
    Bad:
        We measured the distance travelled by the ball to be 14.5m.

    Good:
        We measured the distance travelled by the ball to be 14.5~m.
    """
    return [m.span() for m in matches]

@rule(r"(?<![a-zA-Z\\])(sin|cos|tan|log|max|min)(?![a-zA-Z])", in_env="math")
def check_unescaped_named_math_operators(text, matches):
    r"""関数の名前の前にバックスラッシュを追加してください．例：`\min`

    Example
    -------
    Bad:
        The famous trignometric identity: $sin^2(x) + cos^2(x) = 1$.

    Good:
        The famous trignometric identity: $\\sin^2(x) + \\cos^2(x) = 1$.
    """
    return [m.span() for m in matches]

@rule(r"\b(e\.g\.|i\.e\.)\s+")
def check_abbreviation_innerword_spacing(text, matches):
    r"""省略や例をあげる場合は直後に`\\ `(backslash space)を入力してください．

    Example
    -------
    Bad:
        This shows that new technological gadgets, e.g. smart phones, decrease
        the attention span of young adults.

    Good:
        This shows that new technological gadgets, e.g.\\\\ smart phones,
        decrease the attention span of young adults.
    """
    return [m.span() for m in matches]

@rule(r"\\def\\")
def check_def_command(text, matches):
    r"""`\def`ではなく`\newcommand`を使用してください．"""
    return [m.span() for m in matches]

@rule(r"\\sloppy")
def check_sloppy_command(text, matches):
    r"""`\sloppy`を使わないでください．"""
    return [m.span() for m in matches]

@rule(r",\s*\.\.\.\s*,", in_env="math")
def check_dot_dot_dot_maths(text, matches):
    r"""math環境でのコンマ間の省略は`\ldots`を使用します．"""
    return [m.span() for m in matches]

@rule(r"[+-]\s*\.\.\.\s*[+-]", in_env="math")
def check_dot_dot_dot_maths(text, matches):
    r"""math環境での+-間の省略は`\cdots`を使用します．"""
    return [m.span() for m in matches]

@rule(r"(?<!\\url{)(\bhttps?://)[^\s.]+\.[-A-Za-z0-9+&@#/%?=~_|!:,.;]+")
def check_bare_urls(text, matches):
    r"""URLは`\url`コマンドで囲います．"""
    return [m.span() for m in matches]

@rule(r"[\(（]\\ref{")
def check_bracket_ref(text, matches):
    r"""`\ref`を括弧で囲わなくても，`\eqref`を使えば自動で括弧がつきます．"""
    return [m.span() for m in matches]

@rule(r"\\chapter{.+・.+}|\\section{.+・.+}|\\subsection{.+・.+}|\\subsubsection{.+・.+}")
def check_title_multiple_enumeration(text, matches):
    r"""タイトルで`・`を使って複数列挙しないでください．"""
    return [m.span() for m in matches]

@rule_generator()
def check_incorrect_abbreviations():
    """Punctuate abbreviations correctly. Should be "{0}"."""

    changes = {
        r"et\. al\.": "et al.",
        r"etc[^\.]": "etc.",
        r"i\.e[^\.]": "i.e.",
        r"e\.g[^\.]": "e.g.",
        r"Dr\.": "Dr",
    }

    for incorrect, correct in changes.items():
        yield r"\b" + incorrect + r"\b", correct

@rule_generator()
def check_obsolete_commands():
    """Use the \\{0} command instead."""

    changes = {
        "rm": "textrm",
        "tt": "texttt",
        "it": "textit",
        "bf": "textbf",
        "sc": "textsc",
        "sf": "textsf",
        "sl": "textsl",
        "over": "frac",
        "centerline": "centering",
    }

    for incorrect, correct in changes.items():
        yield r"\\" + incorrect + "{", correct

@rule_generator()
def check_obsolete_packages():
    """Avoid obsolete packages. Use {0} instead."""

    changes = {
        "a4": "a4paper",
        "a4wide": "a4paper",
        "t1enc": r"\usepackage[T1]{fontenc}",
        "umlaute": r"\usepackage[latin1]{inputenc}",
        "isolatin": r"\usepackage[isolatin]{inputenc}",
        "isolatin1": r"\usepackage[latin1]{inputenc}",
        "fancyheadings": "fancyhdr",
        "mathptm": "mathptmx",
        "mathpple": "mathpazo",
        "epsf": "graphicx",
        "epsfig": "graphicx",
        "doublespace": "setspace",
        "scrpage": "scrpage2",
    }

    for incorrect, correct in changes.items():
        yield r"\\" + incorrect + "{", correct

@rule_generator()
def check_obsolete_environments():
    """Use the {0} instead."""

    changes = {"eqnarray": '"align" environment', "appendix": "\\appendix command"}

    for incorrect, correct in changes.items():
        yield r"\begin{" + incorrect + "}", correct

def get_brief(r):
    return r.__doc__.split("\n\n")[0]

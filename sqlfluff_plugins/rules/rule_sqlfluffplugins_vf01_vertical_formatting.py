from typing import List, Optional

from sqlfluff.core.parser import WhitespaceSegment
from sqlfluff.core.rules import BaseRule, LintFix, LintResult, RuleContext
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler


class Rule_SqlfluffPlugins_VF01(BaseRule):
    """
    Enforce vertical formatting in CASE expressions.

    **Target Dialect**: all

    **Description**:
      In complex SQL CASE expressions, inline formatting—where keywords like WHEN and
      THEN reside on the same line—can lead to two issues:

      1. **Reduced Logical Clarity:** Multiple conditions on one line may obscure the
         logical separation between parts of the expression.
      2. **Excessive Line Length:** Inline formatting may cause lines to become
         excessively long, hindering readability.

      This rule enforces vertical formatting by ensuring that the THEN keyword is
      placed on a new line immediately following its corresponding WHEN clause.
      This approach clarifies the logical flow and helps manage line length for improved
      readability.

    **Groups**: all, layout, case, formatting
    """

    code = "VF01"
    name = "vertical_formatting_case"
    description = "Enforce THEN to be on a new line after WHEN (vertical formatting for CASE expressions)."
    groups = ("all", "layout", "case", "formatting")
    crawl_behaviour = SegmentSeekerCrawler({"case_expression"})
    is_fix_compatible = True

    # Hardcoded indent level: add 4 spaces to the WHEN indent.
    INDENT_SPACES = 4

    def _get_token_indent(self, token, case_start_line: int, case_raw: str) -> int:
        """Compute the number of leading spaces on the token's line."""
        lines = case_raw.splitlines()
        line_index = token.pos_marker.line_no - case_start_line
        if 0 <= line_index < len(lines):
            line = lines[line_index]
            return len(line) - len(line.lstrip(" "))
        return 0

    def _fix_inline_clause(
        self, when_token, then_token, segments, case_start_line: int, case_raw: str
    ) -> Optional[LintFix]:
        """Determine and return the LintFix for an inline WHEN-THEN clause, or None if not needed."""
        try:
            idx_then = segments.index(then_token)
        except ValueError:
            return None

        # If whitespace immediately before THEN already contains a newline, assume it is fixed.
        if idx_then > 0 and segments[idx_then - 1].is_type("whitespace"):
            if "\n" in segments[idx_then - 1].raw:
                return None

        # Calculate the indent for THEN: base indent from WHEN plus a fixed indent.
        when_indent = self._get_token_indent(when_token, case_start_line, case_raw)
        then_indent = when_indent + self.INDENT_SPACES
        new_ws = "\n" + " " * then_indent

        if idx_then > 0 and segments[idx_then - 1].is_type("whitespace"):
            return LintFix.replace(
                segments[idx_then - 1],
                [WhitespaceSegment(new_ws)],
            )
        else:
            return LintFix.create_before(
                then_token,
                [WhitespaceSegment(new_ws)],
            )

    def _eval(self, context: RuleContext) -> Optional[List[LintResult]]:
        # Process only CASE expressions.
        if not context.segment.is_type("case_expression"):
            return None

        violations: List[LintResult] = []
        case_start_line = context.segment.pos_marker.line_no
        case_raw = context.segment.raw
        when_clauses = list(context.segment.recursive_crawl("when_clause"))

        for when_clause in when_clauses:
            when_token = None
            then_token = None
            segments = when_clause.segments

            # Identify WHEN and THEN tokens.
            for seg in segments:
                if seg.is_type("keyword") and seg.raw_upper == "WHEN":
                    when_token = seg
                elif seg.is_type("keyword") and seg.raw_upper == "THEN":
                    then_token = seg

            # Only process if both tokens exist and are on the same line.
            if (
                when_token
                and then_token
                and when_token.pos_marker
                and then_token.pos_marker
                and when_token.pos_marker.line_no == then_token.pos_marker.line_no
            ):
                fix = self._fix_inline_clause(when_token, then_token, segments, case_start_line, case_raw)
                if fix:
                    violations.append(
                        LintResult(
                            anchor=then_token,
                            fixes=[fix],
                            description=(
                                "Vertical formatting violation: THEN must appear on a new line "
                                "after WHEN (inline not allowed)."
                            ),
                        )
                    )

        return violations or None

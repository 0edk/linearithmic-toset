import itertools
import math
from typing import Iterable, Optional

from anki.models import TemplateDict
from anki.notes import NoteId
import aqt

from .flashcard_topology import indices, NoteTopology, TopologyDialog
from .gui import TosetViewDialog
from .models import exp_separated, triad_template

class TosetTopology(NoteTopology):
    @staticmethod
    def description() -> str:
        return "Sequence Ordering"

    def make_templates(self, order: int) -> Iterable[TemplateDict]:
        manager = self.mw.col.models
        return itertools.chain(*((
            lambda i=i: (triad_template(manager, i, j)
            for j in indices(order) if exp_separated(i, j))
        )() for i in indices(order)))

    @staticmethod
    def make_fields(order: int) -> Iterable[str]:
        return itertools.chain(
            ("Context", "Source", "Forward", "Backward"),
            (f"Item {i}" for i in indices(order)),
        )

    def custom_css(self, order: int) -> str:
        return "#rl > span ~ span::before { content: \", \"; }\n"

    @staticmethod
    def next_order(order: Optional[int] = None) -> int:
        if order is None:
            return 4
        elif math.log2(order).is_integer():
            return (3 * order) // 2
        else:
            return (4 * order) // 3

    @staticmethod
    def measure_order(fields: dict[str, str]) -> int:
        i = 1
        while f"Item {i}" in fields:
            i += 1
        return i - 1

    def make_editor(
        self, fields: dict[str, str], note_id: Optional[NoteId]
    ) -> TopologyDialog:
        return TosetViewDialog(fields, note_id, self)

TosetTopology(aqt.mw)

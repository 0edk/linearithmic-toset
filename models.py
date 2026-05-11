from anki.models import ModelManager, TemplateDict

def triad_template(manager: ModelManager, i: int, j: int) -> TemplateDict:
    template = manager.new_template(f"Card {i} {j}")
    k = (i + j) // 2
    template["qfmt"] = (
        f"{{{{#Item {i}}}}}{{{{#Item {k}}}}}{{{{#Item {j}}}}}"
        "<strong>{{Context}}</strong> <span id=\"rl\">"
        + "".join(f"<span>{{{{Item {n}}}}}</span>" for n in (i, k, j))
        + "</span> <strong>{{Backward}} to {{Forward}}</strong>"
        "<script src=\"shuffle.js\"></script>"
        f"{{{{/Item {j}}}}}{{{{/Item {k}}}}}{{{{/Item {i}}}}}"
    )
    template["afmt"] = (f"{{{{FrontSide}}}}\n<hr id=answer>\n"
        f"{{{{Item {i}}}}}, {{{{Item {k}}}}}, {{{{Item {j}}}}}")
    return template

def exp_separated(i: int, j: int) -> bool:
    d = j - i
    return d >= 2 and d & (d - 1) == 0

from anki.models import ModelManager, TemplateDict

def arrow_template(manager: ModelManager, i: int, j: int) -> TemplateDict:
    template = manager.new_template(f"Card {i} {j}")
    template["qfmt"] = (f"{{{{#Item {i}}}}}{{{{#Item {j}}}}}"
        f"<strong>{{{{Context}}}}</strong> "
        f"{{{{Item {i}}}}} <strong>→</strong> {{{{Item {j}}}}}"
        f"{{{{/Item {j}}}}}{{{{/Item {i}}}}}")
    template["afmt"] = (f"{{{{FrontSide}}}}\n<hr id=answer>\n"
        f"{{{{{"Forward" if i < j else "Backward"}}}}}")
    print("making template", repr(template["qfmt"]), repr(template["afmt"]))
    return template

def exp_separated(i: int, j: int) -> bool:
    d = abs(i - j)
    return d != 0 and d & (d - 1) == 0

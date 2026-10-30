import src.templates as templates

def format(data):
    strings = [
        templates.HEADER,
        _format_heading(data.get("heading", {})),
        _format_population_section(data.get("population", {})),
        _format_text_section(templates.OFFICERS_UPDATES, data.get("officers", {})),
        _format_text_section(templates.MODERATION_UPDATES, data.get("moderation", {})),
        _format_text_section(templates.CABINET_UPDATES, data.get("cabinet", {})),
        _format_text_section(templates.COMMISSION_UPDATES, data.get("commission", {})),
        _format_a_table(data.get("ga", {})),
        _format_a_table(data.get("sc", {})),
        _format_b_table(data.get("authorships", {})),
        _format_poll_section(data.get("poll", {})),
        templates.FOOTER
    ]

    return "".join(strings)

def _format_heading(heading):
    return templates.REPORT_HEADING.format(
        month=heading.get("month"),
        year=heading.get("year")
    )

def _format_population_section(population):
    return ""

def _format_text_section(template, data):
    return template.format(text=data.get("text"))

def _format_a_table(template, table):
    return ""

def _format_b_table(template, table):
    return ""

def _format_poll_section(results):
    return ""
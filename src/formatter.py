from datetime import datetime
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
        templates.WA_SECTION_HEADING,
        _format_a_table(templates.GA_TABLE, data.get("ga", {})),
        _format_a_table(templates.SC_TABLE, data.get("sc", {})),
        _format_b_table(templates.AUTHORSHIPS_TABLE, data.get("authorships", {})),
        _format_poll_section(data.get("poll", {})),
        templates.FOOTER
    ]

    return "".join(strings)

def _format_heading(heading):
    return templates.REPORT_HEADING.format(
        month=heading.get("month"),
        year=heading.get("year")
    )

def _set_change(current, past):
	c = int(current)
	p = int(past)
	if c >= p:
		return templates.GREEN.format(num=c - p)
	
	return templates.RED.format(num=abs(c - p))

def _format_population_section(data):
	return templates.POPULATION_SECTION.format(
		pop=data.get("current_pop"),
		pop_change=_set_change(data.get("current_pop"), data.get("past_pop")),
		wa=data.get("current_wa"),
		wa_change=_set_change(data.get("current_wa"), data.get("past_wa")),
		endo=data.get("current_endorsements"),
		endo_change=_set_change(data.get("current_endo"), data.get("past_endo")),
		yield_rate=data.get("current_yield"),
		yield_change=_set_change(data.get("current_yield"), data.get("past_yield")),
	)

def _format_text_section(template, data):
    return template.format(text=data.get("text"))

def _format_a_table(template, data):
	rows = []

	if data.get("active") == True:
		for row in data.get("table"):
			if row[2] == "FOR":
				vote = templates.FOR
			else:
				vote = templates.AGAINST

			rows.append(templates.A_TABLE_ROW.format(resolution=row[0], 
									  			   author=row[1],
									  			   vote=vote))
		return template.format(rows="".join(rows))
	else:
		return ""

def _format_b_table(template, data):
	rows = []

	if data.get("active") is True:
		for row in data.get("table"):
			row.append(templates.B_TABLE_ROW.format(resolution=row.get("resolution"),
									  			   author=row.get("author")))

		return template.format(rows="".join(rows))
	else:
		return ""

def _format_poll_results(data):
	results = []

	for result in data:
		results.append(templates.RESULT.format(
			officer=result.get("officer"),
			vote=result.get("vote")
		))

	return "".join(results)

def _format_poll_section(data):
	section = templates.APPROVAL_SECTION.format(
			    valid_votes=data.get("votes", {}).get("valid_votes"),
			    total_votes=data.get("votes", {}).get("total_votes"),
			    ratings_list= _format_poll_results(data.get("officers")),
			    image_url=data.get("image_url"),
                update_date=datetime.now().strftime("%B %d"))
	return section
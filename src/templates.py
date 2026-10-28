HEADER = "[b][size=125][color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=502154][color=#1D2951]GOVERNMENT[/color][/url] [background=#1D2951][color=#1D2951]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440742][color=#FFFFFF]HOME OFFICE[/color][/url]  [color=#1D2951]|[/color][/background] [url=https://www.nationstates.net/page=dispatch/id=1159686][color=#1D2951]FOREIGN OFFICE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1417217][color=#1D2951]WA OFFICE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=529274][color=#1D2951]DISPATCHES[/color][/url] [color=#FFFFFF]|[/color][/size][/b][background-block=#1D2951][centre][IMG]https://raw.githubusercontent.com/ifly6/ifly-images/master/nationstates/europe/headers/header-home-office.png[/IMG][/centre][/background-block][b][size=125][color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440742][color=#1D2951]ABOUT[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440747][color=#1D2951]STAFF[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1443005][color=#1D2951]MODERATION COMMITTEE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1441872][color=#1D2951]EVENTS[/color][/url] [background=#1D2951][color=#1D2951]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1441879][color=#FFFFFF]REPORTS[/color][/url] [color=#1D2951]|[/color][/background] [url=https://www.nationstates.net/page=dispatch/id=1732299][color=#1D2951]EDUCATION[/color][/url] [color=#FFFFFF]|[/color][/size][/b]"
FOOTER = "[background-block=#1D2951][centre][img]https://raw.githubusercontent.com/ifly6/ifly-images/master/nationstates/europe/headers/footer.png[/img][url=http://www.nationstates.net/page=dispatch/id=501996][color=white][b]Welcome[/b][/color][/url] [color=white]|[/color] [url=http://www.nationstates.net/page=dispatch/id=502154][color=white][b]Government[/b][/color][/url] [color=white]|[/color] [url=https://www.nationstates.net/page=dispatch/id=529274][color=white][b]Dispatches[/b][/color][/url][/centre][/background-block]"
REPORT_HEADING = """[center][color=#1D2951][size=150]European State of the Region Report[/size][/color]
                    [color=#1D2951][size=120]{month} {year}[/size][/color][/center]"""
POPULATION_BOX = """[box][u]Regional Population Data[/u]
                    Total Population: {total_pop} ([color=green]+{total_pop_change}[/color])
                    WA Population: {wa_pop} ([color=green]+{wa_pop_change}[/color])
                    Delegate Endorsements: {endorsements} ([color=green]+{endorse_change}[/color])
                    Yield Rate: {yield_rate} ([color=red]{yield_change}[/color])"""
REGIONAL_UPDATES = """[u]Regional Officers Update[/u]
                      {text}"""
MODERATION_UPDATES = """[u]Regional Officers Update[/u]
                      {text}"""
CABINET_UPDATES = """[u]Regional Officers Update[/u]
                      {text}"""
COMMISSION_UPDATES = """[u]Regional Officers Update[/u]
                      {text}"""
WA_ROW_TEMPLATE = "[tr][td]{resolution}[/td][td][nation]{author}[/nation][/td][td]{vote_color}[/td][/tr]"

WA_SECTION = """[u]World Assembly Activity[/u]
                [i]Delegate GA Votes:[/i]
                [table]
                [tr][td]Resolution[/td][td]Author[/td][td]Delegate Vote[/td][/tr]
                {ga_rows}
                [/table]

                [i]Delegate SC Votes:[/i]
                [table]
                [tr][td]Resolution[/td][td]Author[/td][td]Delegate Vote[/td][/tr]
                {sc_rows}
                [/table] 

                [i]European Authorships:[/i]
                {authorships_text}[/box]"""
APPROVAL_SECTION = """[u]European Government Approval Rates[/u]
                      [i]Valid votes out of total votes: {valid_votes}/{total_votes}[/i]
                      {ratings_list}
                      Overall Rate: {very_good_pct}% Very Good, {good_pct}% Good,{mixed_pct}% Mixed.
                      [img]{chart_url}[/img]
                      [align=right][size=60][i]Updated on {update_date}. Census record from {census_source}.[/i][/size][/align][/box]"""
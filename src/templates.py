HEADER = "[b][size=125][color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=502154][color=#1D2951]GOVERNMENT[/color][/url] [background=#1D2951][color=#1D2951]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440742][color=#FFFFFF]HOME OFFICE[/color][/url]  [color=#1D2951]|[/color][/background] [url=https://www.nationstates.net/page=dispatch/id=1159686][color=#1D2951]FOREIGN OFFICE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1417217][color=#1D2951]WA OFFICE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=529274][color=#1D2951]DISPATCHES[/color][/url] [color=#FFFFFF]|[/color][/size][/b][background-block=#1D2951][centre][IMG]https://raw.githubusercontent.com/ifly6/ifly-images/master/nationstates/europe/headers/header-home-office.png[/IMG][/centre][/background-block][b][size=125][color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440742][color=#1D2951]ABOUT[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1440747][color=#1D2951]STAFF[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1443005][color=#1D2951]MODERATION COMMITTEE[/color][/url] [color=#FFFFFF]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1441872][color=#1D2951]EVENTS[/color][/url] [background=#1D2951][color=#1D2951]|[/color] [url=https://www.nationstates.net/page=dispatch/id=1441879][color=#FFFFFF]REPORTS[/color][/url] [color=#1D2951]|[/color][/background] [url=https://www.nationstates.net/page=dispatch/id=1732299][color=#1D2951]EDUCATION[/color][/url] [color=#FFFFFF]|[/color][/size][/b]"

FOOTER = "[background-block=#1D2951][centre][img]https://raw.githubusercontent.com/ifly6/ifly-images/master/nationstates/europe/headers/footer.png[/img][url=http://www.nationstates.net/page=dispatch/id=501996][color=white][b]Welcome[/b][/color][/url] [color=white]|[/color] [url=http://www.nationstates.net/page=dispatch/id=502154][color=white][b]Government[/b][/color][/url] [color=white]|[/color] [url=https://www.nationstates.net/page=dispatch/id=529274][color=white][b]Dispatches[/b][/color][/url][/centre][/background-block]"

REPORT_HEADING = """[center][color=#1D2951][size=150]European State of the Region Report[/size][/color]
                    [color=#1D2951][size=120]{month} {year}[/size][/color][/center]"""

GREEN = "[color=green]+{num}[/color]"

RED = "[color=red]-{num}[/color]"

POPULATION_SECTION = """[box][u]Regional Population Data[/u]
                    Total Population: {pop} ({pop_change})
                    WA Population: {wa} ({wa_change})
                    Delegate Endorsements: {endo} ({endo_change})
                    Yield Rate: {yield_rate} ({yield_change})\n"""

OFFICERS_UPDATES = """[u]Regional Officers Updates[/u]
                      {text}\n"""

MODERATION_UPDATES = """[u]Moderation Updates[/u]
                      {text}\n"""

CABINET_UPDATES = """[u]Cabinet Updates[/u]
                      {text}\n"""

COMMISSION_UPDATES = """[u]Commission Updates[/u]
                      {text}\n"""

A_TABLE_ROW = "[tr][td]{resolution}[/td][td][nation]{author}[/nation][/td][td]{vote}[/td][/tr]"

B_TABLE_ROW = "[tr][td]{resolution}[/td][td][nation]{author}[/nation][/td][/tr]"

FOR = "[color=blue]FOR[/color]"

AGAINST = "[color=red]AGAINST[/color]"

WA_SECTION_HEADING = "[u]World Assembly Activity[/u]\n"

GA_TABLE = """[i]Delegate GA Votes:[/i]
              [table]
              [tr][td]Resolution[/td][td]Author[/td][td]Delegate Vote[/td][/tr]
              {rows}
              [/table]\n"""

SC_TABLE = """[i]Delegate SC Votes:[/i]
                [table]
                [tr][td]Resolution[/td][td]Author[/td][td]Delegate Vote[/td][/tr]
                {rows}
                [/table]\n""" 

AUTHORSHIPS_TABLE = """[i]European Autorships:[/i]
                       [table]
                       [tr][td]Resolution[/td][td]Author[/td][/tr]
                       {rows}
                       [/table]\n"""

RESULT = "[nation]{office}[/nation]: {vote}\n"

APPROVAL_SECTION = """[u]European Government Approval Rates[/u]
                      [i]Valid votes out of total votes: {valid_votes}/{total_votes}[/i]
                      {ratings_list}
                      [img]{image_url}[/img]
                      [align=right][size=60][i]Updated on {update_date}. Census record from ifly6.ip.org.[/i][/size][/align][/box]\n"""
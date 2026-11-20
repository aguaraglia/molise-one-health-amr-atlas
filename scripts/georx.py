import re
GEO=re.compile(r"\bMolise\b|\bMolisan\w*|\bCampobasso\b|\bIsernia\b|\bTermoli\b|\bVenafro\b|\bAgnone\b|\bLarino\b|\bBoi?jano\b|\bBoiano\b|\bTrivento\b|Montenero di Bisaccia|Guglionesi|Campomarino|\bBiferno\b|\bTrigno\b|\bPozzilli\b|Neuromed|Gemelli Molise|Cardarelli (Hospital|Hospital of|Hospital,)? ?(of )?Campobasso|\bIZSAM\b|Abruzzo e (del )?Molise|Abruzzo and Molise",re.I)
WILD=re.compile(r"central Italy|south(ern)?-?central Italy|Apennin\w*|Adriatic|southern Italy",re.I)
AFF=re.compile(r"Campobasso|Isernia|Molise|Termoli|Pozzilli|Venafro|Agnone",re.I)

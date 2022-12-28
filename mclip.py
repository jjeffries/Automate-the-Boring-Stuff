#! python3
# mclip.py - A multiclipboard program.

TEXT = {'free': """Sounds great. My calendar is up to date. Pick time at your convenience and send me an invite. \n\nThanks,\n-Josh""",
        'kickoff': """I look forward to working with you on the assessment next week. Please let me know if you have any questions about the document request or remote access details. On kickoff we will . . .""",
        'complete': """Thank you for the opportunity to work with you on this assessment project. As you review report details, reach out with any questions. The reports have been uploaded to \n\nThanks,\n-Josh"""
        }

import sys, pprint, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    print('KEYPHRASE OPTIONS'.center(25, '='))
    pprint.pprint(TEXT)
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)
    print('KEYPHRASE OPTIONS'.center(25, '='))
    pprint(TEXT)

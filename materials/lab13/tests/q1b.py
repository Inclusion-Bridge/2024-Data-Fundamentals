OK_FORMAT = True
test = {   'name': 'q1b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(answer1b, list)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([isinstance(elt, str) for elt in answer1b])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(answer1b) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all([elt in calls['OFFENSE'].values for elt in answer1b])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> set([a.strip().upper() for a in answer1b]) == set(['THEFT FELONY (OVER $950)', 'THEFT FROM PERSON', 'THEFT MISD. (UNDER $950)'])\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

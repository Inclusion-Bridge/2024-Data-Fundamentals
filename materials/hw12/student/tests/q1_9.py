OK_FORMAT = True
test = {   'name': 'q1_9',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(prob_furd) in set([float, np.float32, np.float64])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Should be a decimal, not a percentage;\n>>> 0 <= prob_furd <= 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.round(prob_furd, 3) == 0.428\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
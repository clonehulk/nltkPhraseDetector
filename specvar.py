


class Variables(object):

    def __init__(self):
        self.cut_of_segmented_reports = [[[u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'n\xe3o', u'tem', u'chuveiro'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'UNCATEGORIZED']], [[u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'A', u'estrutura', u'\xe9', u'satisfat\xf3ria'], [u'UNCATEGORIZED']], [[u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'UNCATEGORIZED']], [[u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'UNCATEGORIZED']]]
        self.topics = ['DISCENTE', 'DOCENTE', 'INFRAESTRUTURA', 'UNCATEGORIZED']
        self.aggregated_topics = [[u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DISCENTE'], [u'Os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'DOCENTE'], [u'O', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'Os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'n\xe3o', u'tem', u'chuveiro'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'A', u'estrutura', u'\xe9', u'satisfat\xf3ria'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'INFRAESTRUTURA'], [u'A', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'O', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'O', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'H\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina']]
        self.dict_of_sentences_by_topic = {'DOCENTE': [[u'o', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'o', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'o', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio'], [u'o', u'quadro', u'de', u'docentes', u'\xe9', u'formado', u'exclusivamente', u'por', u'doutores'], [u'os', u'docentes', u'est\xe3o', u'insatisfeitos', u'com', u'o', u'sal\xe1rio']], 'INFRAESTRUTURA': [[u'a', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'o', u'banheiro', u'n\xe3o', u'tem', u'chuveiro'], [u'o', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'h\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'a', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'o', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'h\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'a', u'estrutura', u'\xe9', u'satisfat\xf3ria'], [u'a', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'o', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'o', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'h\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina'], [u'a', u'infraestrutura', u'est\xe1', u'\xf3tima'], [u'o', u'banheiro', u'est\xe1', u'em', u'condi\xe7\xf5es', u'razo\xe1veis'], [u'o', u'vesti\xe1rio', u'est\xe1', u'em', u'p\xe9ssimas', u'condi\xe7\xf5es'], [u'h\xe1', u'muitos', u'azulejos', u'quebrados', u'na', u'piscina']], 'DISCENTE': [[u'os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia'], [u'os', u'discentes', u'tem', u'apresentado', u'rendimento', u'acima', u'da', u'm\xe9dia']]}
        self.tagged_unigrams_by_topic = {'DOCENTE': [[(u'o', u'ART'), (u'quadro', u'N'), (u'de', u'PREP'), (u'docentes', None), (u'\xe9', u'V'), (u'formado', u'PCP'), (u'exclusivamente', u'ADV'), (u'por', u'PREP|+'), (u'doutores', None)], [(u'os', u'ART'), (u'docentes', None), (u'est\xe3o', u'VAUX'), (u'insatisfeitos', None), (u'com', u'PREP'), (u'o', u'ART'), (u'sal\xe1rio', u'N')], [(u'o', u'ART'), (u'quadro', u'N'), (u'de', u'PREP'), (u'docentes', None), (u'\xe9', u'V'), (u'formado', u'PCP'), (u'exclusivamente', u'ADV'), (u'por', u'PREP|+'), (u'doutores', None)], [(u'os', u'ART'), (u'docentes', None), (u'est\xe3o', u'VAUX'), (u'insatisfeitos', None), (u'com', u'PREP'), (u'o', u'ART'), (u'sal\xe1rio', u'N')], [(u'o', u'ART'), (u'quadro', u'N'), (u'de', u'PREP'), (u'docentes', None), (u'\xe9', u'V'), (u'formado', u'PCP'), (u'exclusivamente', u'ADV'), (u'por', u'PREP|+'), (u'doutores', None)], [(u'os', u'ART'), (u'docentes', None), (u'est\xe3o', u'VAUX'), (u'insatisfeitos', None), (u'com', u'PREP'), (u'o', u'ART'), (u'sal\xe1rio', u'N')], [(u'o', u'ART'), (u'quadro', u'N'), (u'de', u'PREP'), (u'docentes', None), (u'\xe9', u'V'), (u'formado', u'PCP'), (u'exclusivamente', u'ADV'), (u'por', u'PREP|+'), (u'doutores', None)], [(u'os', u'ART'), (u'docentes', None), (u'est\xe3o', u'VAUX'), (u'insatisfeitos', None), (u'com', u'PREP'), (u'o', u'ART'), (u'sal\xe1rio', u'N')]], 'INFRAESTRUTURA': [[(u'a', u'ART'), (u'infraestrutura', None), (u'est\xe1', u'V'), (u'\xf3tima', None)], [(u'o', u'ART'), (u'banheiro', None), (u'n\xe3o', u'ADV'), (u'tem', u'V'), (u'chuveiro', None)], [(u'o', u'ART'), (u'vesti\xe1rio', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'p\xe9ssimas', None), (u'condi\xe7\xf5es', u'N')], [(u'h\xe1', u'V'), (u'muitos', u'PROADJ'), (u'azulejos', None), (u'quebrados', u'N'), (u'na', u'ADV'), (u'piscina', None)], [(u'a', u'ART'), (u'infraestrutura', None), (u'est\xe1', u'V'), (u'\xf3tima', None)], [(u'o', u'ART'), (u'vesti\xe1rio', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'p\xe9ssimas', None), (u'condi\xe7\xf5es', u'N')], [(u'h\xe1', u'V'), (u'muitos', u'PROADJ'), (u'azulejos', None), (u'quebrados', u'N'), (u'na', u'ADV'), (u'piscina', None)], [(u'a', u'ART'), (u'estrutura', u'N'), (u'\xe9', u'V'), (u'satisfat\xf3ria', u'ADJ')], [(u'a', u'ART'), (u'infraestrutura', None), (u'est\xe1', u'V'), (u'\xf3tima', None)], [(u'o', u'ART'), (u'banheiro', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'condi\xe7\xf5es', u'N'), (u'razo\xe1veis', None)], [(u'o', u'ART'), (u'vesti\xe1rio', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'p\xe9ssimas', None), (u'condi\xe7\xf5es', u'N')], [(u'h\xe1', u'V'), (u'muitos', u'PROADJ'), (u'azulejos', None), (u'quebrados', u'N'), (u'na', u'ADV'), (u'piscina', None)], [(u'a', u'ART'), (u'infraestrutura', None), (u'est\xe1', u'V'), (u'\xf3tima', None)], [(u'o', u'ART'), (u'banheiro', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'condi\xe7\xf5es', u'N'), (u'razo\xe1veis', None)], [(u'o', u'ART'), (u'vesti\xe1rio', None), (u'est\xe1', u'V'), (u'em', u'PREP|+'), (u'p\xe9ssimas', None), (u'condi\xe7\xf5es', u'N')], [(u'h\xe1', u'V'), (u'muitos', u'PROADJ'), (u'azulejos', None), (u'quebrados', u'N'), (u'na', u'ADV'), (u'piscina', None)]], 'DISCENTE': [[(u'os', u'ART'), (u'discentes', None), (u'tem', u'V'), (u'apresentado', u'PCP'), (u'rendimento', u'N'), (u'acima', u'PREP'), (u'da', u'NPROP'), (u'm\xe9dia', u'N')], [(u'os', u'ART'), (u'discentes', None), (u'tem', u'V'), (u'apresentado', u'PCP'), (u'rendimento', u'N'), (u'acima', u'PREP'), (u'da', u'NPROP'), (u'm\xe9dia', u'N')], [(u'os', u'ART'), (u'discentes', None), (u'tem', u'V'), (u'apresentado', u'PCP'), (u'rendimento', u'N'), (u'acima', u'PREP'), (u'da', u'NPROP'), (u'm\xe9dia', u'N')], [(u'os', u'ART'), (u'discentes', None), (u'tem', u'V'), (u'apresentado', u'PCP'), (u'rendimento', u'N'), (u'acima', u'PREP'), (u'da', u'NPROP'), (u'm\xe9dia', u'N')]]}
        self.nouns_unigrams_by_topic = {'DOCENTE': [[u'quadro'], [u'sal\xe1rio'], [u'quadro'], [u'sal\xe1rio'], [u'quadro'], [u'sal\xe1rio'], [u'quadro'], [u'sal\xe1rio']], 'INFRAESTRUTURA': [[u'condi\xe7\xf5es'], [u'quebrados'], [u'condi\xe7\xf5es'], [u'quebrados'], [u'estrutura'], [u'condi\xe7\xf5es'], [u'condi\xe7\xf5es'], [u'quebrados'], [u'condi\xe7\xf5es'], [u'condi\xe7\xf5es'], [u'quebrados']], 'DISCENTE': [[u'rendimento', u'm\xe9dia'], [u'rendimento', u'm\xe9dia'], [u'rendimento', u'm\xe9dia'], [u'rendimento', u'm\xe9dia']]}
        self.none_unigrams_by_topic = {'DOCENTE': [[u'docentes', u'doutores'], [u'docentes', u'insatisfeitos'], [u'docentes', u'doutores'], [u'docentes', u'insatisfeitos'], [u'docentes', u'doutores'], [u'docentes', u'insatisfeitos'], [u'docentes', u'doutores'], [u'docentes', u'insatisfeitos']], 'INFRAESTRUTURA': [[u'infraestrutura', u'\xf3tima'], [u'banheiro', u'chuveiro'], [u'vesti\xe1rio', u'p\xe9ssimas'], [u'azulejos', u'piscina'], [u'infraestrutura', u'\xf3tima'], [u'vesti\xe1rio', u'p\xe9ssimas'], [u'azulejos', u'piscina'], [u'infraestrutura', u'\xf3tima'], [u'banheiro', u'razo\xe1veis'], [u'vesti\xe1rio', u'p\xe9ssimas'], [u'azulejos', u'piscina'], [u'infraestrutura', u'\xf3tima'], [u'banheiro', u'razo\xe1veis'], [u'vesti\xe1rio', u'p\xe9ssimas'], [u'azulejos', u'piscina']], 'DISCENTE': [[u'discentes'], [u'discentes'], [u'discentes'], [u'discentes']]}
        self.dict_model_by_topic = {'DOCENTE': {u'docentes': None, u'quadro': u'N', u'sal\xe1rio': u'N', u'de': u'PREP', u'por': u'PREP|+', u'doutores': None, u'insatisfeitos': None, u'formado': u'PCP', u'est\xe3o': u'VAUX', u'\xe9': u'V', u'com': u'PREP', u'o': u'ART', u'exclusivamente': u'ADV', u'os': u'ART'}, 'INFRAESTRUTURA': {u'em': u'PREP|+', u'est\xe1': u'V', u'razo\xe1veis': None, u'\xf3tima': None, u'infraestrutura': None, u'n\xe3o': u'ADV', u'condi\xe7\xf5es': u'N', u'h\xe1': u'V', u'tem': u'V', u'a': u'ART', u'chuveiro': None, u'piscina': None, u'p\xe9ssimas': None, u'\xe9': u'V', u'muitos': u'PROADJ', u'vesti\xe1rio': None, u'azulejos': None, u'o': u'ART', u'quebrados': u'N', u'satisfat\xf3ria': u'ADJ', u'estrutura': u'N', u'banheiro': None, u'na': u'ADV'}, 'DISCENTE': {u'tem': u'V', u'acima': u'PREP', u'discentes': None, u'rendimento': u'N', u'm\xe9dia': u'N', u'da': u'NPROP', u'apresentado': u'PCP', u'os': u'ART'}}
        self.tagger_accuracy_by_topic = {'DOCENTE': 0.12264328554907077, 'DISCENTE': 0.016711044171306134, 'INFRAESTRUTURA': 0.12410460539881481}
        self.run_time_most_frequent_nouns_unigrams_by_topic = {'DOCENTE': [u'quadro', u'sal\xe1rio'], 'DISCENTE': [u'm\xe9dia', u'rendimento'], 'INFRAESTRUTURA': [u'condi\xe7\xf5es', u'quebrados']}
        self.run_time_wordtypes_of_none_unigrams_by_topic = {'DOCENTE': [u'insatisfeitos', u'docentes', u'doutores'], 'INFRAESTRUTURA': [u'piscina', u'\xf3tima', u'p\xe9ssimas', u'vesti\xe1rio', u'azulejos', u'razo\xe1veis', u'infraestrutura', u'banheiro', u'chuveiro'], 'DISCENTE': [u'discentes']}





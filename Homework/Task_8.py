import re


def main(s):
    start_tag = '<data> '
    end_tag = '</data>'
    s = s.replace(start_tag, '').replace(end_tag, '').replace('\n', ' ')
    s = re.split(r"\.\s*done;", s)
    s.pop(-1)
    keys = []
    val_res = []
    for item in s:
        pattern_declaration = r"do declare\s?(.*?)\<\|"
        pattern_values = r"\{([^}]*)\}"
        key = re.search(pattern_declaration, item).group(1)
        key = key.replace(" ", "")
        keys.append(key)
        values_match = re.search(pattern_values, item)
        values = [v.strip().strip("'") for v in
                  values_match.group(1).split(',')]
        val_res.append(values)
    f_res = dict(zip(keys, val_res))
    return f_res

    # s_res = '{'
    # for i, (key, value) in enumerate(f_res.items()):
    #     value_str = ', '.join(f"'{v}'" for v in value)
    #     s_res += f"'{key}': [{value_str}]" \
    #         if i == 0 else f",\n '{key}': [{value_str}]"
    # s_res += '}'
    # return s_res


# print(main(
#     "<data> do declare usre <| { 'enadi_149' , 'onla_457' , 'dige_657','quesaza' }. done; do declare soce <| {'xeer' , 'ribe_997' ,'aten_645' ,'atbice_564' }. done; </data>"))
# print(main(
#     "<data>do declare isesat_28 <| {'usve' , 'rete_424' , 'edares_380','esus' }. done; do declare onle_214 <| {'male_935' ,'tedite_663' }. done;do declare edge_210 <| { 'xedi_171' , 'indi_573' , 'ditidi_588','ansoxe'}. done;do declare geraen_375 <|{ 'isesar' ,'zati' , 'vesote', 'usgedi'}. done; </data>"))
print(main("<data> do declare orbi_711<|{ 'usbece_969' ,'orla' ,'axera_111'\n,'esen' }. done; do declare esle<|{ 'atedon_297' ,'ceanti_65' , 'dima'\n}. done; do declare geor <|{ 'atza_143' , 'usor' }. done;do declare\ntein_442 <| {'laon_447', 'eres_584' , 'laar_159'}. done; </data>"))

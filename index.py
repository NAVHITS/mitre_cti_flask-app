from stix2 import FileSystemSource, Filter, parse
import json

fs = FileSystemSource('./cti/enterprise-attack')

def get_techniques_by_platform(src, platform):
    return src.query([
        Filter('type', '=', 'attack-pattern'),
        Filter('x_mitre_platforms', '=', platform)
        
    ])

def get_mitigations_by_technique(src, tech_stix_id):
    relations = src.relationships(tech_stix_id, 'mitigates', target_only=True)
    return src.query([
        Filter('type', '=', 'course-of-action'),
        Filter('id', 'in', [r.source_ref for r in relations])
    ])

def get_technique_by_id(src, id):
    filt = [
        Filter('type', '=', 'attack-pattern'),
        Filter('external_references.external_id', '=', id)
    ]
    return src.query(filt)

def get_technique_by_name(src, name):
    filt = [
        Filter('type', '=', 'attack-pattern'),
        Filter('name', '=', name)
    ]
    return src.query(filt)

def get_tactic_techniques(src, tactic):
    techs =  src.query([
        Filter('type', '=', 'attack-pattern'),
        Filter('kill_chain_phases.phase_name', '=', tactic)
    ])

    # double checking the kill chain is MITRE ATT&CK
    return [t for t in techs if {
            'kill_chain_name' : 'mitre-attack',
            'phase_name' : tactic,
    } in t.kill_chain_phases]




# tech = get_technique_by_id(fs, 'T1049')
# t = get_mitigations_by_technique(fs, tech[0]['id'])
# for i in t:
#     print(i['name'])
#     print(i['description'])



from flask import Flask
from flask import render_template, request
from index import get_mitigations_by_technique, get_techniques_by_platform, fs, get_technique_by_id, get_tactic_techniques




app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def attack_details():
    result = request.form.to_dict()
    res = result['Platform']
    aws_attack_pattern = get_techniques_by_platform(fs, res)
    # print(aws_attack_pattern)
    
    return render_template('result.html', result = aws_attack_pattern, name = res)
 
@app.route('/details/<aid>')
def info(aid):
    attack_id = aid
    t = get_technique_by_id(fs, attack_id)
    m = get_mitigations_by_technique(fs, t[0]['id'])
    kc = t[0]['kill_chain_phases'][0]['phase_name']
    
    return render_template('details.html', result = t, aid = attack_id, kc = kc.capitalize(), m = m)

@app.route('/tactics/<tname>')
def tactics_list(tname):
    tactics_name = tname
    d = get_tactic_techniques(fs, tactics_name)
    return render_template('tactics.html', res = d, tn = tactics_name)


if __name__ == "__main__":
    app.run()
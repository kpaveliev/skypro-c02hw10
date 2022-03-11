from flask import Flask
import utils

# Import candidates dictionary and assign elements to a class
candidates = utils.assign_class('candidates.json')

# Starting Flask
app = Flask(__name__)

# Main page - candidates list
@app.route("/")
def page_index():
    text = chr(10).join([candidates[i].print_candidate()
                         for i in range(len(candidates))])
    return f'<h1>Список кандидатов</h1>'\
           f'<pre>{text}</pre>'

# Candidate page
@app.route("/candidate/<int:id>")
def page_candidate(id):
    return f'<img src={candidates[id-1].picture}>'\
           f'<pre>{candidates[id-1].print_candidate()}</pre>'

# Skill search page
@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    text = chr(10).join([candidates[i].print_candidate()
                         for i in range(len(candidates))
                         if skill_name in candidates[i].skills.lower()])
    return f'<h1>Список кандидатов c навыком {skill_name}</h1>'\
           f'<pre>{text}</pre>'

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template
import utils

app = Flask(__name__)

not_found_page = "not_found.html"

candidateDB = utils.CandidateManager()
candidateDB.load_candidates_from_json('candidates.json')


@app.route("/")
def page_index():
    return render_template("list.html", candidates=candidateDB.candidates)


@app.route("/candidate/<int:uid>")
def page_single(uid):
    candidate = candidateDB.get_candidate(uid)
    if candidate is not None:
        return render_template("single.html", candidate=candidate)
    else:
        return render_template(not_found_page)


@app.route("/search/<candidate_name>")
def page_search(candidate_name):
    candidates = candidateDB.get_candidates_by_name(candidate_name)
    if candidates is None:
        return render_template(not_found_page)
    return render_template("search.html", number_of_candidates=len(candidates), candidates=candidates)


@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates = candidateDB.get_candidates_by_skill(skill_name)
    if candidates is None:
        return render_template(not_found_page)
    return render_template("skill.html", skill_name=skill_name, num_candidates=len(candidates), candidates=candidates)


app.run(debug=True)

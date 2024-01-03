from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load data from the existing JSON file
with open('superList.json', 'r') as fp:
    superList = json.load(fp)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_teams', methods=['POST'])
def compare_teams():
    team1 = request.json['team1']
    team2 = request.json['team2']

    team1_players = findAllTeam(team1)
    team2_players = findAllTeam(team2)
    
    common_players = common_member(team1_players, team2_players)

    return jsonify({'common_players': list(common_players)})

def findAllTeam(teamName):
    ret = []
    for year in superList:
        yearInfo = superList[year]
        for player in yearInfo:
            attrs = yearInfo[player]
            if attrs[4] == teamName:
                ret.append(player)
    return ret

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

def matchTeams (team1, team2):
    team1Players = findAllTeam(team1)
    team2Players = findAllTeam(team2)
    return common_member(team1Players, team2Players)

if __name__ == '__main__':
    app.run(debug=True)

async function compareTeams() {
    const team1 = document.getElementById('team1').value;
    const team2 = document.getElementById('team2').value;

    const response = await fetch('/compare_teams', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ team1, team2 }),
    });

    const data = await response.json();
    const playersList = document.getElementById('playersList');
    playersList.innerHTML = '';

    if (data.common_players.length > 0) {
        data.common_players.forEach(player => {
            const listItem = document.createElement('li');
            listItem.textContent = player;
            playersList.appendChild(listItem);
        });
    } else {
        const listItem = document.createElement('li');
        listItem.textContent = "No player was ever on both of these teams";
        playersList.appendChild(listItem);
    }
}

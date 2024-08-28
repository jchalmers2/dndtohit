function rollDice(diceRoll) {
    const regex = /^(\d*)d(\d+)([-+]\d+)?$/;
    const match = diceRoll.match(regex);
    if (!match) {
        throw new Error("Invalid dice format");
    }

    const numDice = parseInt(match[1] || '1', 10);
    const diceType = parseInt(match[2], 10);
    const bonus = parseInt(match[3] ? match[3] : '0', 10);

    let total = 0;
    for (let i = 0; i < numDice; i++) {
        total += Math.floor(Math.random() * diceType) + 1;
    }
    total += bonus;

    return total;
}

function attackSimulation(numAttacks, ac, toHitMod, damageDice, advantage) {
    let hits = 0;
    let totalDamage = 0;

    for (let i = 0; i < numAttacks; i++) {
        let attackRoll;
        if (advantage) {
            attackRoll = Math.max(rollDice("1d20"), rollDice("1d20")) + toHitMod;
        } else {
            attackRoll = rollDice("1d20") + toHitMod;
        }

        if (attackRoll >= ac) {
            hits++;
            totalDamage += rollDice(damageDice);
        }
    }

    return { hits, totalDamage };
}

function calculate() {
    const numAttacks = parseInt(document.getElementById('numAttacks').value, 10);
    const ac = parseInt(document.getElementById('ac').value, 10);
    const toHitMod = parseInt(document.getElementById('toHitMod').value, 10);
    const damageDice = document.getElementById('damageDice').value;
    const advantage = document.getElementById('advantage').value === 'yes';

    try {
        const { hits, totalDamage } = attackSimulation(numAttacks, ac, toHitMod, damageDice, advantage);
        document.getElementById('numHits').innerText = `Number of Hits: ${hits}`;
        document.getElementById('totalDamage').innerText = `Total Damage: ${totalDamage}`;
    } catch (error) {
        alert(error.message);
    }
}

function clearResults() {
    document.getElementById('numAttacks').value = '';
    document.getElementById('ac').value = '';
    document.getElementById('toHitMod').value = '';
    document.getElementById('damageDice').value = '';
    document.getElementById('advantage').value = 'no';
    document.getElementById('numHits').innerText = '';
    document.getElementById('totalDamage').innerText = '';
}

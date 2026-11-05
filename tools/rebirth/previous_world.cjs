// Exact, reversible Rebirth projection for older preservation fixtures only.
// test_rebirth.cjs checks the current implementation and the same change set.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const assert = require('assert');
const canonical = v => Array.isArray(v) ? v.map(canonical) : v && typeof v === 'object' ? Object.fromEntries(Object.keys(v).sort().map(k => [k, canonical(v[k])])) : v;
const hash = v => crypto.createHash('sha256').update(JSON.stringify(canonical(v))).digest('hex');
module.exports = function previousWorld(world) {
    world = require('../ardelis/previous_world.cjs')(world);
    if (!world.traits?.['Summoned one']) return world;
    const review = JSON.parse(fs.readFileSync(path.join(__dirname, 'review.json'), 'utf8'));
    assert.strictEqual(hash(world), review.afterHash, 'Only the exact reviewed Rebirth revision can enter the historical fixture');
    const old = structuredClone(world);
    for (const row of review.rows) {
        let parent = old;
        for (const key of row.path.slice(0, -1)) parent = parent[key];
        const key = row.path.at(-1);
        if (row.kind === 'removed') parent[key] = structuredClone(row.before);
        else {
            assert.strictEqual(hash(parent[key]), row.afterHash, 'Reviewed Rebirth field ' + row.path.join('/'));
            if (row.kind === 'added') delete parent[key];
            else parent[key] = structuredClone(row.before);
        }
    }
    assert.strictEqual(hash(old), review.baseHash, 'Historical view must reconstruct the approved Universal Fishing world exactly');
    return old;
};

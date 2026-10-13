/* Run with node; verifies pure logic, NOT EBPro. */
const assert=require('assert'),u=require('./meter_analytics.js');
const ok=value=>({value,quality:'GOOD'}),bad=value=>({value,quality:'COMM_TIMEOUT'});
assert.strictEqual(u.selectMeter(61).privateIndex0,7680);
assert.throws(()=>u.selectMeter(62));
assert.strictEqual(u.imbalance([ok(90),ok(100),ok(110)]).value,10);
assert.strictEqual(u.imbalance([ok(90),bad(100),ok(110)]).state,'N_A');
assert.strictEqual(u.apparent(ok(3),ok(4)).value,5);
assert.strictEqual(u.pf(ok(0),ok(0)).state,'N_A');
assert.strictEqual(u.coverage(0,10).value,0);
assert.strictEqual(u.coverage(0,0).state,'N_A');
let r=u.historyRequest({meter:2,metric:'power_a_kw',allowedMetrics:['power_a_kw'],from:'2026-10-01T00:00:00Z',to:'2026-10-02T00:00:00Z',id:4});
assert.strictEqual(r.sqlText,null);
assert.throws(()=>u.historyRequest({...r,from:'2020-01-01T00:00:00Z'}));
assert.strictEqual(u.acceptHistory(r,{meter:2,id:4,ok:true,rows:[1]},1,4).accepted,false);
assert.strictEqual(u.acceptHistory(r,{meter:2,id:4,ok:true,rows:[1]},2,4).accepted,true);
console.log('OFFLINE PASS: UCS analyzer JS math and query guard checks; no HMI proof.');

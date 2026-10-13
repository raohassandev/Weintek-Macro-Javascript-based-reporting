/*
UCS USB1 controlled write/read check — run ON DEMAND as an EBPro JS Action on
Local HMI only. Tested? NO. Check cMT SVRX/FHDX and EBPro >= 6.09.01 first.
Sets one U16 status value through this.config.ProbeStatus mapped to LW-8250.
0=UNTESTED, 1=FAILED, 2=BYTE-FOR-BYTE PASSED.
Does NOT verify SQLite, data sampling, backup, fsync after power failure,
SMART, or all 61 meters. Repeat after reconnect and enforce TTL in UCS UI.
Never schedule high-frequency writes (media wear).
SDK: https://dl.weintek.com/public/Document/JS_Object_SDK/Current/module-%40weintek_libc_stdio.html
*/
const stdio = await import("@weintek/libc/stdio");
const fs = await import("@weintek/filesystem");

async function ucsProbeUsb1() {
  const target = "USB1";
  // Never overwrite a production log: unique, isolated 32-byte test file.
  const path = "/_ucs_probe_" + Date.now() + ".txt";
  const data = new TextEncoder().encode("UCS_PROBE|" + Date.now());
  let writer = null;
  let reader = null;
  let verified = false;
  try {
    writer = stdio.fopen(target, path, "w");
    const written = stdio.fwrite(writer, data.buffer);
    if (written !== data.byteLength) {
      throw new Error("Partial write: " + written + "/" + data.byteLength);
    }
    stdio.fflush(writer);
    if (stdio.ferror(writer) !== 0) throw new Error("Write stream error");
    stdio.fclose(writer);
    writer = null;
    reader = stdio.fopen(target, path, "r");
    const buffer = new ArrayBuffer(data.byteLength);
    const count = stdio.fread(reader, buffer);
    if (count !== data.byteLength) throw new Error("Short read: " + count);
    const received = new Uint8Array(buffer);
    verified = received.every((value, index) => value === data[index]);
    if (!verified) throw new Error("Readback content mismatch");
    console.log("UCS USB byte-for-byte readback: PASS (not persisted historian proof)");
  } catch (error) {
    console.log("UCS USB read/write verification failed:", error.message);
  } finally {
    if (reader !== null) try { stdio.fclose(reader); } catch (e) { console.log(e.message); }
    if (writer !== null) try { stdio.fclose(writer); } catch (e) { console.log(e.message); }
    // Only remove this run's own isolated file, never enumerate/remove customer files.
    try { if (fs.exists(target, path)) fs.remove(target, path); } catch (e) { console.log("Probe cleanup:", e.message); }
  }
  // This status MUST expire independently. UI never interprets a latched pass
  // as permanent "storage working". LW-8251 freshness is maintained separately.
  try {
    await driver.promises.setData(this.config.ProbeStatus, [verified ? 2 : 1]);
  } catch (error) {
    console.log("UCS probe status publish failed:", error.message);
  }
  return verified;
}

// EBPro JS Action invokes this source in Local HMI context when an authorized
// "Verify Storage" action is requested. Avoid Viewer/client-side execution.
await ucsProbeUsb1();

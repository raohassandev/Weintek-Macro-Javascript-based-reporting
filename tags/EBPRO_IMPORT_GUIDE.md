# Weintek Address Tag Library import boundary
This repository's `resource-manager-dictionary.csv` is a **vendor-neutral engineering dictionary** (name, type, access, provenance, source). It is **not yet guaranteed** to be importable directly as EasyBuilder Pro's CSV.

Official procedure from WeintekUSA:
1. In actual target EasyBuilder Pro, create 3 tags manually under `Project → Address`: e.g. LB-12048 Bit, LW-9076 UInt32, LW-9025 UInt16, and **Export CSV** with UTF-8 selected.
2. Compare the exported columns/word-type encodings in that actual version against this dictionary (Weintek support instructs exactly this).
3. Use `tools/map_address_tags.py --template exported-tags.csv --source tags/resource-manager-dictionary.csv --output /tmp/ucs_ebpro_import.csv` after configuring column mapping. **The current tool deliberately refuses to guess unknown headers**.
4. In a test EBPro project, Import CSV, validate three tags and object data formats. Do not automatically overwrite live tags without a project backup.
5. For newer eMMC tags gray/unsupported in Address Tag Library, omit them from the imported tag set.

Sources: [Address Tag Library](https://dl.weintek.com/public/EBPro/UserManual/eng/UserManual_separate_chapter/Chapter-16-Address-Tag-Library-UserManual-eng.pdf); [Weintek USA support on CSV format](https://forum.weintekusa.com/t/why-cant-i-import-my-user-defined-tags-into-easybuilder-pro/624).

cat $1 | jq -c 'select(.IsDir==false) | {bucket: (.Path | split("/")[0]), path: (.Path | split("/")[1:] | join("/")), size: .Size, url: "https://462000828.lumidata.eu/\(.Path)"}' >manifest.jsonl

cat manifest.jsonl | grep -E '(html|lang|text|metadata).zst|pdf.warc.gz|robotstxt.warc.gz|.warc.gz' >download_manifest_cc.jsonl

TOCS = {}

MESSAGES = {
    "0001": "activation",
    "0002": "cancellation",
    "0003": "movement",
    "0004": "_unidentified",
    "0005": "reinstatement",
    "0006": "origin change",
    "0007": "identity change",
    "0008": "_location change"
}

# Trust Frame Example:
# Train ID: 861N33MM21 (1N33 M) 
# Message Type: movement      
# TOC: 88 
# Loc Stanox: @86301  
# Platform: 2 

def print_trust_frame(parsed):
    body = parsed["body"]

    toc = parsed["body"].get("toc_id", '')
    platform = parsed["body"].get("platform", '')
    loc_stanox = "@" + body.get("loc_stanox", "")

    summary = "{} ({} {}) {:<13s} {:2s} {:<6s} {:3s}".format(
        body["train_id"], body["train_id"][2:6], body["train_id"][6],
        MESSAGES[parsed["header"]["msg_type"]], toc, loc_stanox, platform)
    
    print(summary)


def extract_trust_fields(parsed):
    try:
        body = parsed["body"]
        header = parsed["header"]
        train_id = body.get("train_id", '')
        msg_type = header.get("msg_type", '')
        return train_id, msg_type
    except Exception as e:
        print("Malformed message caused the following error:", e)
        return "", ""

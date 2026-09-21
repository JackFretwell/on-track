import db
import json
from models import Location

engine = db.get_engine()
session = db.create_session(engine)
print("SCRIPT STARTED")
try:
    with open('CORPUSExtract.json') as f:
        corpus_extract = json.load(f)
        locations = list(corpus_extract.values())[0]
        duplicate = {}

        print(len(locations))
        for location in locations:
            try:
                stanox = location.get("STANOX", None).strip()
                uic = location.get("UIC", None)
                three_alpha = location.get("3ALPHA", None)
                tiploc = location.get("TIPLOC", None).strip()
                nlc = location.get("NLC", None)
                nlc_description = location.get("NLCDESC", None)

                if tiploc == '':
                    continue

                if tiploc in duplicate:
                    continue
                
                db.create_location(session, stanox, uic, three_alpha, tiploc, nlc, nlc_description)
                duplicate[tiploc] = ""
                
            except Exception as e:
                print("An error occurred when adding location to DB:\n", e)
                continue
        session.commit()
        print("Done, committed.")
finally:
    session.close()


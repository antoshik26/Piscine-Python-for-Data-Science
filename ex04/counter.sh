echo '"name","count"' > hh_uniq_positions.csv
cut -f 3 -d ',' ../ex03/hh_positions.csv | sort | uniq -ci | awk  '{print $2","$1}' >> hh_uniq_positions.csv
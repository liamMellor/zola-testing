for f in UnitTesting/zola_testing/* UnitTesting/zola_testing/*/* UnitTesting/zola_testing/*/*/*; do
  if [ "${f: -3:3}" != ".py" ] || [ "$(basename $f)" == "__init__.py" ]; then
    ## This is either not a python script, or it is the special __init__.py script, so skip it
    continue;
  fi;
  f=${f:0:$((${#f}-3))};  ## remove the ".py" extension
   python -m unittest ${f//\//.};  ## substitute "/" with "."
done
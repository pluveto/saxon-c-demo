LIBSAXON_DIR=$(pwd)/libsaxon

export PATH=$PATH:$LIBSAXON_DIR/command
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIBSAXON_DIR/libs/nix

SCRIPT_DIR=$(pwd)/demo

pushd $SCRIPT_DIR

    start_time="$(date -u +%s.%N)"

    transform -s:input-large.xml -xsl:xml2json.xsl -o:output.json

    end_time="$(date -u +%s.%N)"
    elapsed_time=$(echo "($end_time - $start_time) * 1000" | bc)
    echo "$elapsed_time ms"

popd
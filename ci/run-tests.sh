#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
cat > reports/junit.xml <<'XML'
<testsuite name="vm2-protected-main-public" tests="1" failures="1">
  <testcase classname="vm2.protected.main.silent.runner.public" name="20260915" time="0.001">
    <failure message="quarantined test failed">VM2 controlled quarantined failure</failure>
  </testcase>
</testsuite>
XML
echo "VM2 controlled independent runner/test-driver failure"
exit 42

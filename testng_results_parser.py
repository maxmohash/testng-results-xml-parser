from lxml import etree
import urllib
url = "http://example.com/testng-results.xml"
root = etree.parse(urllib.urlopen(url))


def failed_tests_data():
    failed_test_run_duration = []
    failed_test_name = []
    failed_test_run_date = []
    failed_test_stacktrace = []
    for failure in root.xpath('/testng-results/suite/test/class/test-method[@status="FAIL"]'):
        failed_test_run_duration.append(failure.attrib['duration-ms'])
        failed_test_name.append(failure.attrib['name'])
        failed_test_run_date.append(failure.attrib['started-at'])
        failed_test_stacktrace.append(failure.find('./exception/full-stacktrace').text)

    print "\n"
    print "No of failed tests =", len(failed_test_stacktrace)
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Names of all failed tests :", failed_test_name
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Failed tests run duration :", failed_test_run_duration
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Failed tests run date :", failed_test_run_date
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Failed tests stacktrace :", failed_test_stacktrace
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    failed_name_duration = dict((k, v) for k, v in zip(failed_test_name, failed_test_run_duration))
    failed_name_date = dict((x, y) for x, y in zip(failed_test_name, failed_test_run_date))
    failed_name_stacktrace = dict((p, q) for p, q in zip(failed_test_name, failed_test_stacktrace))
    print "Dict of failed tests name and run date :", failed_name_date
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Dict of failed test names and their respective run duration :", failed_name_duration
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Dict of failed test names and their respective exception stacktrace :", failed_name_stacktrace

print "\n"
print "Here the failed tests data will be printed", failed_tests_data()
print "\n"


def passed_tests_data():
    passed_test_name = []
    passed_test_run_duration = []
    passed_test_run_date = []
    for passed in root.xpath('/testng-results/suite/test/class/test-method[@status="PASS"]'):
        if passed.attrib['name'] != "tearDownMethod" and passed.attrib['name'] != "setup":
            for x in root.xpath('/testng-results/suite/test/class/test-method/params/param/value'):
                if "TestResult" in x.text:
                    if (x.text.split("=")[1:][0]).rstrip("status").rstrip(" ") not in passed_test_name:
                        passed_test_name.append((x.text.split("=")[1:][0]).rstrip("status").rstrip(" "))
                        passed_test_run_duration.append(passed.attrib['duration-ms'])
                        passed_test_run_date.append(passed.attrib['started-at'])

    print "No of passed tests =", len(passed_test_name)
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Names of passed tests :", passed_test_name
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Passed tests run duration :", passed_test_run_duration
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Passed tests run date :", passed_test_run_date
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    passed_name_duration = dict((k, v) for k, v in zip(passed_test_name, passed_test_run_duration))
    passed_name_date = dict((x, y) for x, y in zip(passed_test_name, passed_test_run_date))
    print "Dict of passed tests name and run date :", passed_name_date
    print "__________________________________________________________________________________________________________" \
          "____________________________________________________________________________________________________________"
    print "\n"
    print "Dict of passed test names and their respective run duration :", passed_name_duration

print "Here the passed tests data will be printed :", passed_tests_data()
print "\n"




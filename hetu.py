import datetime
import re
import sys

CHECKSUM_CHARS = "0123456789ABCDEFHJKLMNPRSTUVWXY"
MIN_DATE = datetime.date(1800, 1, 1)
MAX_DATE = datetime.date(2999, 12, 31)

def usage():
    print >> sys.stderr, "Usage: {0} date1 date2".format(sys.argv[0])
    print >> sys.stderr, "Dates must be in YYYY-MM-DD format and between years 1800 and 2999."
    print >> sys.stderr, "Date1 cannot be after date2."
    return 1

def parse_date(text):
    match = re.match("^(\d{1,4})-(\d{1,2})-(\d{1,2})$", text)
    if match != None:
        year, month, day = map(int, match.groups())
        return datetime.date(year, month, day)
    else:
        raise ValueError("invalid date syntax")

def is_allowed_date(date):
    return MIN_DATE <= date <= MAX_DATE

def date_range(date1, date2):
    date = date1
    while date <= date2:
        yield date
        date += date.resolution

class Percent(object):
    def __init__(self, num, denom):
        self.value = float(num) / denom * 100
    
    def __str__(self):
        return "{0:.2f}%".format(self.value)
    
def histogram(f, xs):
    h = {}
    for x in xs:
        histogram_add(h, f(x))
    return h

def histogram_add(h, y, n = 1):
    h[y] = n + h.setdefault(y, 0)

def histogram_extend(h1, h2):
    for k, v in h2.iteritems():
        histogram_add(h1, k, v)

def histogram_show(label, h):
    blank = " " * len(label)
    lines = []
    n = len(h)
    i = 0
    for k in sorted(h.keys()):
        if i % 6 == 0:
            lines.append(label if i == 0 else blank)
        lines[-1] += " {0} -> {1}".format(k, h[k]) + ("." if i == n-1 else ",")
        i += 1
    return "\n".join(lines)

def global_histogram(histograms):
    h_g = {}
    for h in histograms:
        histogram_extend(h_g, h)
    return h_g

def frequency_histogram(h):
    total = sum(h.itervalues())
    h_freq = {}
    for k, v in h.iteritems():
        h_freq[k] = Percent(v, total)
    return h_freq

def show_fm(h_f, h_m):
    return histogram_show("F:", h_f) + "\n" + histogram_show("M:", h_m)

def indent(text, n):
    lines = []
    for line in text.split("\n"):
        lines.append(" " * n + line)
    return "\n".join(lines)

def checksum(date, n):
    assert is_allowed_date(date)
    assert 1 <= n <= 999
    year_term = 10**3 * (date.year % 100)
    month_term = 10**5 * date.month
    day_term = 10**7 * date.day
    i = (year_term + month_term + day_term + n) % 31
    return CHECKSUM_CHARS[i]

def main():
    if len(sys.argv) != 3:
        return usage()
    
    prog, date1text, date2text = sys.argv
    try:
        date1, date2 = map(parse_date, (date1text, date2text))
    except ValueError:
        return usage()

    if not (is_allowed_date(date1) and is_allowed_date(date2)) or date2 < date1:
        return usage()
    
    histograms_f = {}
    histograms_m = {}
    for date in date_range(date1, date2):
        print date
                
        csum = lambda n: checksum(date, n)
        evens = xrange(1, 1000, 2)
        odds = xrange(2, 1000, 2)
        
        h_f = histogram(csum, evens)
        h_m = histogram(csum, odds)
        histograms_f[date] = h_f
        histograms_m[date] = h_m
        print indent(show_fm(h_f, h_m), 2)
        print
    
    h_f_g = frequency_histogram(global_histogram(histograms_f.itervalues()))
    h_m_g = frequency_histogram(global_histogram(histograms_m.itervalues()))
    
    print "Overall frequencies"
    print indent(show_fm(h_f_g, h_m_g), 2)    

if __name__ == "__main__":
    sys.exit(main())
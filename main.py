import sys
sys.dont_write_bytecode = True

# import modules.reminders as reminders
# reminders.clearReminders()

import modules.intentclassification as ICRNN
ICRNN.word2vec()
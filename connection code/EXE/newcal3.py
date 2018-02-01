import time
import atom
import gdata
import gdata.calendar
import gdata.calendar.service


def GetCalendarByTitle(calendar_service, title):
  feed = calendar_service.GetAllCalendarsFeed()
  calendar = [entry for entry in feed.entry if entry.title.text == title][0]
  return calendar
  
def InsertEvent(calendar_service, calendar, title,
                      content, start_time=None, end_time=None):
    event = gdata.calendar.CalendarEventEntry()
    event.title = atom.Title(text=title)
    event.content = atom.Content(text=content)

    if start_time is None:
      # Use current time for the start_time and have the event last 1 hour
      start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
      end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time() + 3600))
    event.when.append(gdata.calendar.When(start_time=start_time, end_time=end_time))
        
    calendar_id = calendar.id.text.split("/")[-1]
    uri = 'http://www.google.com/calendar/feeds/%(calendar_id)s/private/full' % locals()

    tries = 0 
    while tries < 2:
      try:
        new_event = calendar_service.InsertEvent(event, uri)
        break
      except gdata.service.RequestError:
        tries += 1
    
    print 'New single event inserted: %s' % (new_event.id.text,)
    print '\tEvent edit URL: %s' % (new_event.GetEditLink().href,)
    print '\tEvent HTML URL: %s' % (new_event.GetHtmlLink().href,)
    
    return new_event

if __name__=='__main__':
  calendar_service = gdata.calendar.service.CalendarService()
  calendar_service.email = 'ellenzi166@gmail.com'
  calendar_service.password = '365elY##'
  calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
  calendar_service.ProgrammaticLogin()


  calendar = GetCalendarByTitle(calendar_service, "schedule")
  InsertEvent(calendar_service, calendar, "attend a conference", "classes")
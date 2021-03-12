class MyCalendarThree {
    Map<Integer, Integer> map;
    public MyCalendarThree() {
        map = new TreeMap<>();
    }
    
    public int book(int start, int end) {
        map.put(start, map.getOrDefault(start, 0) + 1);
        map.put(end, map.getOrDefault(end, 0) - 1);
        int activeEvents = 0, maxEvents = 0;
        for (int val : map.values()) {
            activeEvents += val;
            maxEvents = Math.max(maxEvents, activeEvents);
        }
        return maxEvents;
    }
}
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> str1 = new ArrayList<>();
        char[] pSorted = p.toCharArray();
        Arrays.sort(pSorted);

        for (int i = 0; i <= s.length() - p.length(); i++) {
            String str2 = s.substring(i, i + p.length());
            char[] str2Sorted = str2.toCharArray();
            Arrays.sort(str2Sorted);

            if (Arrays.equals(str2Sorted, pSorted)) {
                str1.add(i);
            }
        }

        return str1;
    }
}
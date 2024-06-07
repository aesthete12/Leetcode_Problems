class TrieNode {
  private TrieNode[] children = new TrieNode[26];
  private String word;

  public TrieNode[] getChildren() {
    return children;
  }

  public String getWord() {
    return word;
  }

  public void setWord(String word) {
    this.word = word;
  }
}

class Solution {
  public String replaceWords(List<String> dictionary, String sentence) {
    StringBuilder sb = new StringBuilder();

    for (final String word : dictionary)
      insert(word);

    final String[] words = sentence.split(" ");
    for (final String word : words)
      sb.append(' ').append(search(word));

    return sb.substring(1).toString();
  }

  private TrieNode root = new TrieNode();

  private void insert(final String word) {
    TrieNode node = root;
    for (char c : word.toCharArray()) {
      final int i = c - 'a';
      if (node.getChildren()[i] == null)
        node.getChildren()[i] = new TrieNode();
      node = node.getChildren()[i];
    }
    node.setWord(word);
  }

  private String search(final String word) {
    TrieNode node = root;
    for (char c : word.toCharArray()) {
      if (node.getWord() != null)
        return node.getWord();
      final int i = c - 'a';
      if (node.getChildren()[i] == null)
        return word;
      node = node.getChildren()[i];
    }
    return word;
  }
}

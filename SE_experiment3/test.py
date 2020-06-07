from Dictionary import Dictionary


def test():
    Dict = Dictionary('SE_experiment3/temp.csv')
    assert Dict.getPhonetic('appreciate') == "ә'pri:ʃieit"
    assert Dict.getDefinition('appreciate') == ['v. recognize with gratitude; be grateful for', 'v. be fully aware of; realize fully','v. gain in value','v. increase the value of']
    assert Dict.getTranslation('appreciate') == ['vt. 赏识, 鉴别, 为...而感激, 领会, 欣赏', 'vi. 增值, 涨价']
    assert Dict.getSentences('appreciate') == ['They have come to appreciate it. 他们已经开始在感激它了。', 'I appreciate his efforts and I wish him well. 我感谢他的努力。我祝愿他身体健康。']
    Dict.setSentence('hello', '"Hello," he said uncertainly. “你好，”他迟疑地说。\\nYou: Hello, who just joined? 你：你好，刚刚加入的是谁？')
    Dict.saveTo()


if __name__ == '__main__':
    test()

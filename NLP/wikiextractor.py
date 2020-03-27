import requests
from bs4 import BeautifulSoup
import re


def extract_html(url):
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, "html.parser")
    return soup.prettify()


def remove_tag(section, char1, char2):
    desired = []
    dummy = []
    is_tag = False

    for char in section:

        if char == char1:
            dummy.append(char)
            is_tag = True

        if char == char2:
            dummy.pop()
            if not dummy:
                is_tag = False
                continue

        if is_tag:
            continue
        else:
            desired.append(char)

    return ''.join(desired)


def remove_newline(section):
    return ''.join(section.split("\n"))


def remove_extra_whitespace(section):
    strings = section.split(" ")
    desired_strings = []
    for string in strings:
        if string == '':
            continue
        desired_strings.append(string)

    return ' '.join(desired_strings)


def _extract_section_article(sections):
    new_sections = []
    for section in sections:
        section = section[section.find("<p>"):]
        section = remove_tag(section, "<", ">")
        section = remove_tag(section, "[", "]")
        section = remove_tag(section, "(", ")")
        section = remove_extra_whitespace(remove_newline(section))
        section = remove_xa(section)
        section = remove_dot(section)
        new_sections.append(section)
    return new_sections


def remove_dot(section):
    new_section = []
    strings = section.split(" ")
    for string in strings:
        if string == '' or string[0] == '.':
            continue
        else:
            new_section.append(string)

    return " ".join(new_section)


def remove_substring(section, substring):
    new_section = []
    strings = section.split(" ")
    for string in strings:
        if substring in string:
            new_section.append("".join(string.split(substring)))
        else:
            new_section.append(string)
    return " ".join(new_section)


def remove_xa(section):
    new_section = []
    strings = section.split(" ")
    for string in strings:
        if "\xa0" in string:
            new_section.extend(string.split("\xa0"))
        else:
            new_section.append(string)
    return " ".join(new_section)


def _extract_header(sections):
    headers = []
    for section in sections:
        header = section[:section.find('</h2>')]
        header = remove_tag(header, "<", ">")
        header = remove_newline(header)
        header = remove_extra_whitespace(header)
        headers.append(header)
    return headers


def extract_introduction(html):
    html = html[html.find():html.find("<div id=\"toc\"")]


def _extract_unclean_sections(html):

    h2 = [m.start() for m in re.finditer('<h2>', html)]
    sections = []
    for i, j in list(zip(h2[:-1], h2[1:])):
        sections.append(html[i:j])

    return sections


def extract_intro(html):

    intro = remove_extra_whitespace(html)
    intro = intro[intro.find("<p>\n <b>\n"):intro.find("<div aria-labelledby=\"mw-toc-heading\"")]
    intro = remove_tag(intro, "<", ">")

    intro = remove_tag(intro, "[", "]")
    intro = remove_newline(intro)
    intro = remove_tag(intro, "(", ")")
    intro = remove_extra_whitespace(intro)

    return intro


def extract_wiki(article_name):
   url = "https://en.wikipedia.org/wiki/{}".format(article_name)
   html = extract_html(url)
   wiki = dict()
   intro = extract_intro(html)
   wiki["Introduction"] = intro

   sections = _extract_unclean_sections(html)
   wiki.update({header: article for header, article in zip(_extract_header(sections),_extract_section_article(sections))})

   return wiki






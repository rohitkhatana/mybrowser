##in this file u have all lex ,yacc file imported.
# if u compile it then output of input will be generated in the pdf form
 

webpage = """<html>
<h6>MY OWN BROWSER</h6>
<h2>rohit khatana</h2>
<h1>Level One Headings Use (H1) Tags</h1> 
<p>Paragraphs use (P) tags. Unordered lists use (UL) tags.
<ul>
  <li> List items use (LI) tags. </li> 

  <!-- You should update this HTML until the order and nesting of
      the tags match the reference image. --> 
    <li>Text can be bold<b>(B)</b>,italic<i>(I)</i>,small<small>(SMALL)</small>,big<BIG>(BIG)</BIG>,or look like a typewriter.<tt>(TT)</tt></li>
    <li>there are also ordered list that use (OL) tag.Let's make some nested inside our current item .</li>
    <ol>
        <li>these can also be <bold>strong(STRONG)</bold> or <i>emphasized(EM)</i>, which typically renders like bold and italics.</li>
        <li> webpages can have <a href ="target">hyperlinks (A HREF ="target").</a>   </li>
    </ol>

  <li> It is also possible to include images<img src="cs262.png" /> (IMG SRC="CS262.PNG")</li>
</ul>
</p>
<p>we'll finish off one last paragraph.

</p></html>"""

import ply.lex as lex
import ply.yacc as yacc
import htmltokens
import htmlgrammar
import htmlinterp
import graphics as graphics
import jstokens


def interpret(ast):
    for tree in ast:
        if tree[0] == "word-element":
            graphics.word(tree[1])
        elif tree[0] == "tag-elemnet":
            tagname = tree[1]
            tagargs = tree[2]
            subtree = tree[3]
            closetagname = tree[4]
        if tagname != closename:
            graphics.warning("tagname not match")
        else:
            graphics.begintag(tagname,tagargs)
            interpret(subtree)
            graphics.endtag()
                             
            
        



htmllexer = lex.lex(module=htmltokens) 
htmlparser = yacc.yacc(module=htmlgrammar,tabmodule="parsetabhtml") 
ast = htmlparser.parse(webpage,lexer=htmllexer) 
jslexer = lex.lex(module=jstokens) 
graphics.initialize() # Enables display of output.
htmlinterp.interpret(ast) 
graphics.finalize() # Enables display of output.

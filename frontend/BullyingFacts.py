from SideBarLogo import add_logo
import streamlit as st
# import frontend.pages.tes as tes
st.title("Understanding Bullying: A Harmful Behavior Rooted in Power Imbalances")
st.markdown("""
Bullying, a damaging and aggressive behavior rooted in power imbalances, continues to be a pervasive issue in communities worldwide. Often repeated over time or carrying the potential for recurrence, bullying amplifies its harmful consequences, leaving deep emotional scars.

The ripple effects extend to both victims and perpetrators, with research showing that both groups face heightened risks of long-term psychological, emotional, and social challenges. These consequences often persist into adulthood, impacting mental health, relationships, and overall development.

Experts stress that proactive measures to address and prevent bullying are essential. Creating supportive and inclusive environments can help mitigate its far-reaching effects, fostering healthier communities and brighter futures for all involved.

""",unsafe_allow_html=True)

st.markdown("""**Source:** <a href="https://www.stopbullying.gov/bullying/what-is-bullying#:~:text=Bullying%20is%20unwanted%2C%20aggressive%20behavior,may%20have%20serious%2C%20lasting%20problems">stopbullying.gov</a>""",unsafe_allow_html=True)

st.divider()
st.title("Bullying Types")
col1, col2 = st.columns(2)

with col1:
    st.image("asset/BullyingTypes.jpg")
with col2:
    st.markdown("""
        - **Verbal bullying** involves saying or writing harmful things, such as teasing, name-calling, making inappropriate sexual comments, taunting, or threatening harm. This can extend to cyberbullying through hurtful messages, online harassment, or posting offensive comments on social media. 
        - **Social bullying**, also known as relational bullying, aims to damage a person’s reputation or relationships. This includes excluding someone intentionally, discouraging friendships, spreading rumors, or publicly embarrassing someone. In a cyber context, this can involve spreading false information, creating fake profiles, or sharing private information to harm someone’s social standing. 
        - **Physical bullying** involves causing harm to a person’s body or possessions, such as hitting, kicking, pinching, spitting, tripping, pushing, stealing, or destroying belongings, as well as making rude or mean hand gestures. 
        - **Cyberbullying related** to physical threats may include sending intimidating messages, sharing violent imagery, or inciting others to harm the victim. Each of these types, including their cyber manifestations, can significantly impact the victim’s mental, emotional, and social well-being.

    """, unsafe_allow_html= True)
    st.markdown("""**Source:** <a href="https://www.stopbullying.gov/bullying/what-is-bullying">stopbullying.gov</a>""",unsafe_allow_html=True)


st.divider()

st.title("Bullying Exposed: Uncovering Impact on Lives")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Perpetrators")
    st.markdown("""
    1. Loss of self-confidence and self-esteem.
    2. Increased isolation, feeling disconnected from school or social environments.
    3. Decline in academic performance.
    4. Development of physical health problems.
    5. Mental health challenges, such as depression, anxiety, loneliness, or loss of interest in activities.
    6. In extreme cases, risks of self-harm or suicide.
""")

with col2:
    st.header("Victims")
    st.markdown("""
    1. High levels of aggressive behavior.
    2. Increased likelihood of alcohol and drug addiction.
    3. Greater tendency to engage in criminal activities, such as fighting and property damage.
    4. Potential for abusive behavior toward partners.
    5. Difficulty understanding and respecting boundaries or limits.
""")

with col3:
    st.header("Survivors")
    st.markdown("""
    1. Potential to develop mental health issues, such as anxiety or depression.
    2. Reluctance or fear of attending school or social gatherings
""")
    
# st.markdown("**Source:**")
st.markdown("""
    **Source:**
    <a href="https://bulliesout.com/help-hub/articles/the-effects-of-bullying/">bulliesout.com</a>
    | <a href="https://www.stopbullying.gov/bullying/effects#:~:text=Kids%20who%20are%20bullied%20are,issues%20may%20persist%20into%20adulthood">stopbullying.gov</a>
    | <a href="⁠https://anti-bullyingalliance.org.uk/tools-information/all-about-bullying/prevalence-and-impact-bullying/impact-bullying">anti-bullyingalliance.org.uk</a>
""",unsafe_allow_html=True)


st.divider()
st.title("Caught in the Act: What to Do When You Witness or Experience Bullying")
st.markdown("""
    1. **Report the incident**: Immediately inform a school administrator, such as a teacher, school counselor, or school principal.
    2. **Seek help for extreme cases**: If the situation involves severe harm or danger, contact the police without delay.
    
""", unsafe_allow_html= True)
st.markdown("""**Source:** <a href="https://www.stopbullying.gov/resources/get-help-now">stopbullying.gov</a>""",unsafe_allow_html=True)


st.divider()
st.title("Spotting the Red Flags: Warning Signs of Bullying You Shouldn’t Ignore")
st.markdown("""
    Not all children show clear signs of being bullied, but it's important to watch for these common indicators:
""",unsafe_allow_html=True)

st.markdown("""
    - **Physical signs:** Unexplained injuries or damaged belongings, such as clothing, books, or electronics.
    - **Health issues:** Frequent headaches, stomachaches, or pretending to be ill.
    - **Emotional distress:** Difficulty sleeping or having recurring nightmares.
    - **Academic struggles:** Declining grades, loss of interest in schoolwork, or avoiding school altogether.

""",unsafe_allow_html=True)

st.markdown("""
    Being attentive to these warning signs can help address bullying early and provide the necessary support to children in need
""",unsafe_allow_html=True)

st.markdown("""**Source:** <a href="https://www.cdc.gov/youth-violence/about/about-bullying.html">cdc.gov</a>""",unsafe_allow_html=True)

st.divider()
st.title("Standing Guard: The Crucial Role of Adults in Preventing Bullying")
st.markdown("""Parents, school staff, and other adults play a crucial role in preventing bullying. Here's how they can help:""",unsafe_allow_html=True)
st.markdown("""
    - **Educate about bullying:** Teach kids what bullying is, how to stand up to it safely, and emphasize that it is unacceptable. Ensure they know how to seek help when needed.
    - **Communicate regularly:** Keep open communication by checking in frequently, listening to their concerns, knowing their friends, and understanding their experiences at school.
    - **Encourage hobbies:** Support kids in pursuing activities they enjoy to build confidence, make friends, and reduce vulnerability to bullying.
    - **Be a role model:** Demonstrate kindness and respect in your interactions to teach kids how to treat others.
""",unsafe_allow_html=True)

st.markdown("""**Source:** <a href="https://www.stopbullying.gov/resources/get-help-now">stopbullying.gov</a>""",unsafe_allow_html=True)



st.divider()
st.title("Empowering the Next Generation: Teaching Kids to Tackle Bullying Head-On")
st.markdown("""
    - **Understand and Identify Bullying:** Teach kids what bullying is so they can recognize it and talk about it when it happens to them or others.
    - **Seek Help from Trusted Adults:** Encourage kids to talk to trusted adults who can provide support, advice, and comfort, even if they can’t resolve the issue directly.
    - **Stand Up to Bullies:** Discuss how to respond to bullying confidently, such as using humor, saying “stop” assertively, or walking away if needed.
    - **Practice Safety Strategies:** Teach kids to stay near adults or groups of friends to minimize risks.
    - **Support Peers:** Encourage kindness towards bullied peers and seek help on their behalf.
    - **Engage with Educational Resources:** Encourage kids to watch and discuss materials that enhance their understanding, mental resilience, and positive behavior to effectively handle bullying situations.

""",unsafe_allow_html=True)

st.markdown("""**Source:** <a href="https://www.stopbullying.gov/prevention/how-to-prevent-bullying">stopbullying.gov</a>""",unsafe_allow_html=True)



add_logo()
#!/usr/bin/env python3

# from config import db
from app import app
from models import db, Organizer, Attendee, Event, Review

with app.app_context():

    print("Deleting all records...")
    Organizer.query.delete()
    Attendee.query.delete()
    Review.query.delete()
    Event.query.delete()

    def seed():

        organizer1 = Organizer(
            full_name='Jane Wangari',
            affiliation='Wangari Foundation',
            location='Nairobi',
            contact='0722775059',
            username='Wangari_jane',
            image_url='image1.jpg',
            bio='Founder and CEO of Wangari Foundation',
            user_role='organizer'
        )
        organizer1.password_hash = 'lightbringer'

        organizer2 = Organizer(
            full_name='John Kamau',
            affiliation='Kamau Enterprises',
            location='Nairobi',
            contact='0712345678',
            username='KamauJohn',
            image_url='image2.jpg',
            bio='Entrepreneur and Innovator',
            user_role='organizer'
        )
        organizer2.password_hash = 'innovate123'

        organizer3 = Organizer(
            full_name='Grace Mwende',
            affiliation='Mwende Holdings',
            location='Mombasa',
            contact='0734567890',
            username='GraceM',
            image_url='image3.jpg',
            bio='Passionate about community development',
            user_role='organizer'
        )
        organizer3.password_hash = 'communitylove'

        organizer4 = Organizer(
            full_name='James Mwangi',
            affiliation='Mwangi Tech Solutions',
            location='Nairobi',
            contact='0723456789',
            username='MwangiTech',
            image_url='image4.jpg',
            bio='Tech enthusiast and problem solver',
            user_role='organizer'
        )
        organizer4.password_hash = 'techwizard'

        organizer5 = Organizer(
            full_name='Mary Auma',
            affiliation='Auma Foundation',
            location='Kisumu',
            contact='0711223344',
            username='AumaMary',
            image_url='image5.jpg',
            bio='Dedicated to empowering women',
            user_role='organizer'
        )
        organizer5.password_hash = 'empowerment123'

        organizer6 = Organizer(
            full_name='Pauline Kariuki',
            affiliation='Kariuki Innovations',
            location='Nairobi',
            contact='0756789012',
            username='PaulineK',
            image_url='image6.jpg',
            bio='Innovating for a better tomorrow',
            user_role='organizer'
        )
        organizer6.password_hash = 'innovate2023'
        organizer7 = Organizer(
            full_name='Peter Gitau',
            affiliation='Gitau Solutions',
            location='Nairobi',
            contact='0765432109',
            username='PeterG',
            image_url='image7.jpg',
            bio='Passionate about software development',
            user_role='organizer'
        )
        organizer7.password_hash = 'codingislife'

        organizer8 = Organizer(
            full_name='Mercy Njeri',
            affiliation='Njeri Enterprises',
            location='Nakuru',
            contact='0709123456',
            username='MercyN',
            image_url='image8.jpg',
            bio='Promoting sustainable agriculture',
            user_role='organizer'
        )
        organizer8.password_hash = 'greenplanet'

        organizer9 = Organizer(
            full_name='Samuel Kibet',
            affiliation='Kibet Foundation',
            location='Eldoret',
            contact='0798765432',
            username='SamKibet',
            image_url='image9.jpg',
            bio='Advocating for education for all',
            user_role='organizer'
        )
        organizer9.password_hash = 'educateall'

        organizer10 = Organizer(
            full_name='Anne Wanjiku',
            affiliation='Wanjiku Tech Solutions',
            location='Nairobi',
            contact='0745678901',
            username='AnneW',
            image_url='image10.jpg',
            bio='Empowering youth through technology',
            user_role='organizer'
        )
        organizer10.password_hash = 'youthtech'

        organizer11 = Organizer(
            full_name='Joseph Otieno',
            affiliation='Otieno Enterprises',
            location='Kisumu',
            contact='0776543210',
            username='JosephO',
            image_url='image11.jpg',
            bio='Bringing clean energy solutions',
            user_role='organizer'
        )
        organizer11.password_hash = 'cleanenergy'

        organizer12 = Organizer(
            full_name='Susan Nyambura',
            affiliation='Nyambura Innovations',
            location='Nairobi',
            contact='0701122334',
            username='SusanN',
            image_url='image12.jpg',
            bio='Promoting gender equality in STEM',
            user_role='organizer'
        )
        organizer12.password_hash = 'stemequality'
        organizer13 = Organizer(
            full_name='David Mutisya',
            affiliation='Mutisya Consulting',
            location='Machakos',
            contact='0791122334',
            username='DavidM',
            image_url='image13.jpg',
            bio='Providing business solutions for SMEs',
            user_role='organizer'
        )
        organizer13.password_hash = 'businesssolutions'

        organizer14 = Organizer(
            full_name='Grace Munala',
            affiliation='Muthoni Charities',
            location='Thika',
            contact='0723344556',
            username='GraceiM',
            image_url='image14.jpg',
            bio='Empowering vulnerable communities',
            user_role='organizer'
        )
        organizer14.password_hash = 'communityempowerment'

        organizer15 = Organizer(
            full_name='Brian Muchiri',
            affiliation='Muchiri Innovations',
            location='Nairobi',
            contact='0766778899',
            username='BrianM',
            image_url='image15.jpg',
            bio='Developing cutting-edge software solutions',
            user_role='organizer'
        )
        organizer15.password_hash = 'innovativesolutions'

        organizer16 = Organizer(
            full_name='Alice Njeri',
            affiliation='Njeri Tech Hub',
            location='Kiambu',
            contact='0701020304',
            username='AliceN',
            image_url='image16.jpg',
            bio='Supporting startups and entrepreneurs',
            user_role='organizer'
        )
        organizer16.password_hash = 'startupsupport'

        organizer17 = Organizer(
            full_name='John Karanja',
            affiliation='Karanja Ventures',
            location='Nairobi',
            contact='0733445566',
            username='JohnK',
            image_url='image17.jpg',
            bio='Investing in renewable energy projects',
            user_role='organizer'
        )
        organizer17.password_hash = 'renewableinvestments'

        organizer18 = Organizer(
            full_name='Esther Achieng',
            affiliation='Achieng Foundation',
            location='Kisumu',
            contact='0799556677',
            username='EstherA',
            image_url='image18.jpg',
            bio='Advocating for children\'s rights',
            user_role='organizer'
        )
        organizer18.password_hash = 'childrensrights'

        organizer19 = Organizer(
            full_name='Michael Koech',
            affiliation='Koech Solutions',
            location='Eldoret',
            contact='0722789456',
            username='MichaelK',
            image_url='image19.jpg',
            bio='Providing IT consulting services',
            user_role='organizer'
        )
        organizer19.password_hash = 'itconsulting'

        organizer20 = Organizer(
            full_name='Sarah Wambui',
            affiliation='Wambui Enterprises',
            location='Nairobi',
            contact='0788990011',
            username='SarahW',
            image_url='image20.jpg',
            bio='Promoting sustainable agriculture practices',
            user_role='organizer'
        )
        organizer20.password_hash = 'sustainableagriculture'

        # Create instances of attendees
        attendee1 = Attendee(
            full_name='Alex Wafulla',
            affiliation='Tech bros',
            location='Nairobi',
            contact='0712345678',
            username='wafulla the goat',
            image_url='image1.jpg',
            bio='Aspiring data analyst',
            user_role='attendee',
            invitation_code=1234
        )
        attendee1.password_hash = 'thegoat'

        attendee2 = Attendee(
            full_name='Mary Njoki',
            affiliation='Nairobi University',
            location='Nairobi',
            contact='0798765432',
            username='MaryNj',
            image_url='image2.jpg',
            bio='Studying Computer Science',
            user_role='attendee',
            invitation_code=2345
        )
        attendee2.password_hash = 'csstudent'

        attendee3 = Attendee(
            full_name='Kevin Mwangi',
            affiliation='Tech Innovators',
            location='Nairobi',
            contact='0765432198',
            username='KevinM',
            image_url='image3.jpg',
            bio='Passionate about artificial intelligence',
            user_role='attendee',
            invitation_code=3456
        )
        attendee3.password_hash = 'aienthusiast'

        attendee4 = Attendee(
            full_name='Susan Akinyi',
            affiliation='TechGirls Club',
            location='Kisumu',
            contact='0721987654',
            username='SusanA',
            image_url='image4.jpg',
            bio='Empowering girls in STEM',
            user_role='attendee',
            invitation_code=4567
        )
        attendee4.password_hash = 'stemgirls'

        attendee5 = Attendee(
            full_name='Peter Kamau',
            affiliation='Future Coders Academy',
            location='Nairobi',
            contact='0797654321',
            username='PeterK',
            image_url='image5.jpg',
            bio='Teaching kids how to code',
            user_role='attendee',
            invitation_code=5678
        )
        attendee5.password_hash = 'futurecoder'

        attendee6 = Attendee(
            full_name='Grace Wairimu',
            affiliation='Tech Sisters Foundation',
            location='Eldoret',
            contact='0789345678',
            username='GraceW',
            image_url='image6.jpg',
            bio='Supporting women in tech',
            user_role='attendee',
            invitation_code=6789
        )
        attendee6.password_hash = 'techsister'

        attendee7 = Attendee(
            full_name='Brian Ochieng',
            affiliation='Tech Geeks Community',
            location='Nairobi',
            contact='0765432987',
            username='BrianO',
            image_url='image7.jpg',
            bio='Building tech solutions for social good',
            user_role='attendee',
            invitation_code=7890
        )
        attendee7.password_hash = 'socialtech'

        attendee8 = Attendee(
            full_name='Faith Njeri',
            affiliation='Code Queens Academy',
            location='Nairobi',
            contact='0723456789',
            username='FaithN',
            image_url='image8.jpg',
            bio='Training women to code',
            user_role='attendee',
            invitation_code=8901
        )
        attendee8.password_hash = 'codequeen'

        attendee9 = Attendee(
            full_name='James Mwaura',
            affiliation='Digital Nomads Kenya',
            location='Nairobi',
            contact='0798765432',
            username='JamesM',
            image_url='image9.jpg',
            bio='Working remotely and traveling',
            user_role='attendee',
            invitation_code=9012
        )
        attendee9.password_hash = 'digitalnomad'

        attendee10 = Attendee(
            full_name='Cynthia Akoth',
            affiliation='Tech Ladies Association',
            location='Kisumu',
            contact='0712345678',
            username='CynthiaA',
            image_url='image10.jpg',
            bio='Supporting women in the tech industry',
            user_role='attendee',
            invitation_code=1122
        )
        attendee10.password_hash = 'techlady'
        attendee11 = Attendee(
            full_name='Brian Kimani',
            affiliation='Innovate Africa',
            location='Nairobi',
            contact='0789456123',
            username='BrianK',
            image_url='image11.jpg',
            bio='Promoting innovation across the continent',
            user_role='attendee',
            invitation_code=2233
        )
        attendee11.password_hash = 'innovator'

        attendee12 = Attendee(
            full_name='Sandra Chepkoech',
            affiliation='She Codes Africa',
            location='Eldoret',
            contact='0756789012',
            username='SandraC',
            image_url='image12.jpg',
            bio='Empowering women through coding',
            user_role='attendee',
            invitation_code=3344
        )
        attendee12.password_hash = 'shecodes'

        attendee13 = Attendee(
            full_name='Patrick Maina',
            affiliation='Tech Explorers Club',
            location='Nairobi',
            contact='0721234567',
            username='PatrickM',
            image_url='image13.jpg',
            bio='Discovering new technologies',
            user_role='attendee',
            invitation_code=4455
        )
        attendee13.password_hash = 'techexplorer'

        attendee14 = Attendee(
            full_name='Joyce Wambui',
            affiliation='Code for Change Foundation',
            location='Nairobi',
            contact='0789012345',
            username='JoyceW',
            image_url='image14.jpg',
            bio='Using technology for social impact',
            user_role='attendee',
            invitation_code=5566
        )
        attendee14.password_hash = 'codeforchange'

        attendee15 = Attendee(
            full_name='David Ouma',
            affiliation='Digital Skills Academy',
            location='Kisumu',
            contact='0712345678',
            username='DavidO',
            image_url='image15.jpg',
            bio='Teaching digital skills to youth',
            user_role='attendee',
            invitation_code=6677
        )
        attendee15.password_hash = 'digitalskills'

        attendee16 = Attendee(
            full_name='Grace Njeri',
            affiliation='Techpreneurs Hub',
            location='Nairobi',
            contact='0798765432',
            username='GraceN',
            image_url='image16.jpg',
            bio='Supporting tech startups',
            user_role='attendee',
            invitation_code=7788
        )
        attendee16.password_hash = 'techpreneur'

        attendee17 = Attendee(
            full_name='Peter Njoroge',
            affiliation='Innovation Hub Kenya',
            location='Nairobi',
            contact='0789456123',
            username='PeterN',
            image_url='image17.jpg',
            bio='Fostering a culture of innovation',
            user_role='attendee',
            invitation_code=8899
        )
        attendee17.password_hash = 'innovationhub'

        attendee18 = Attendee(
            full_name='Mercy Achieng',
            affiliation='Tech Solutions Ltd',
            location='Nairobi',
            contact='0756789012',
            username='MercyA',
            image_url='image18.jpg',
            bio='Providing IT solutions for businesses',
            user_role='attendee',
            invitation_code=9900
        )
        attendee18.password_hash = 'techsolutions'

        attendee19 = Attendee(
            full_name='John Kimani',
            affiliation='Startup Incubator Africa',
            location='Nairobi',
            contact='0721234567',
            username='JohnK',
            image_url='image19.jpg',
            bio='Supporting and nurturing startup ideas',
            user_role='attendee',
            invitation_code=1122
        )
        attendee19.password_hash = 'startupincubator'

        attendee20 = Attendee(
            full_name='Lucy Muthoni',
            affiliation='Women in Tech Kenya',
            location='Nairobi',
            contact='0789012345',
            username='LucyM',
            image_url='image20.jpg',
            bio='Empowering women through technology',
            user_role='attendee',
            invitation_code=2233
        )
        attendee20.password_hash = 'womenintech'



        # Create instances of events
        event1 = Event(
            title='Step Into The Tech World',
            logo='logo1.jpg',
            name='Tech Summit',
            location='Mombasa',
            period='22nd April, 2024 - 30th April, 2024',
            event_description='Come lets learn more about technology together.',
            organizer=organizer2,
            attendee = attendee1
        )

        event2 = Event(
            title='AI and Robotics Conference',
            logo='logo2.jpg',
            name='AI and Robotics Conference',
            location='Nairobi',
            period='15th May, 2024 - 17th May, 2024',
            event_description='Explore the latest advancements in AI and robotics.',
            organizer=organizer3,
            attendee=attendee2
        )

        event3 = Event(
            title='Digital Marketing Expo',
            logo='logo3.jpg',
            name='Digital Marketing Expo',
            location='Nairobi',
            period='10th June, 2024 - 12th June, 2024',
            event_description='Discover the latest trends in digital marketing strategies.',
            organizer=organizer1,
            attendee=attendee3
        )

        event4 = Event(
            title='Blockchain Summit',
            logo='logo4.jpg',
            name='Blockchain Summit',
            location='Strathmore University',
            period='20th July, 2024 - 22nd July, 2024',
            event_description='Learn about the transformative potential of blockchain technology.',
            organizer=organizer2,
            attendee=attendee4
        )

        event5 = Event(
            title='Cybersecurity Conference',
            logo='logo5.jpg',
            name='Cybersecurity Conference',
            location='Eldoret',
            period='5th August, 2024 - 7th August, 2024',
            event_description='Explore the latest trends and challenges in cybersecurity.',
            organizer=organizer3,
            attendee=attendee5
        )

        event6 = Event(
            title='Data Science Symposium',
            logo='logo6.jpg',
            name='Data Science Symposium',
            location='Westlands',
            period='15th September, 2024 - 17th September, 2024',
            event_description='Deep dive into the world of data science and analytics.',
            organizer=organizer1,
            attendee=attendee6
        )

        event7 = Event(
            title='Mobile App Development Workshop',
            logo='logo7.jpg',
            name='Mobile App Development Workshop',
            location='Upperhill',
            period='10th October, 2024 - 12th October, 2024',
            event_description='Learn to build innovative mobile applications from industry experts.',
            organizer=organizer2,
            attendee=attendee7
        )

        event8 = Event(
            title='Cloud Computing Summit',
            logo='logo8.jpg',
            name='Cloud Computing Summit',
            location='Kileleshwa',
            period='20th November, 2024 - 22nd November, 2024',
            event_description='Explore the latest advancements in cloud computing technologies.',
            organizer=organizer3,
            attendee=attendee8
        )

        event9 = Event(
            title='Fintech Forum',
            logo='logo9.jpg',
            name='Fintech Forum',
            location='Kenyatta University',
            period='5th December, 2024 - 7th December, 2024',
            event_description='Discover the future of financial technology and innovation.',
            organizer=organizer1,
            attendee=attendee9
        )

        event10 = Event(
            title='E-commerce Conference',
            logo='logo10.jpg',
            name='E-commerce Conference',
            location='Two Rivers',
            period='10th January, 2025 - 12th January, 2025',
            event_description='Explore the latest trends and strategies in e-commerce industry.',
            organizer=organizer2,
            attendee=attendee10
        )
        event11 = Event(
            title='Artificial Intelligence Summit',
            logo='logo11.jpg',
            name='AI Summit',
            location='Junction Mall',
            period='15th February, 2025 - 17th February, 2025',
            event_description='Explore the cutting-edge applications of artificial intelligence.',
            organizer=organizer3,
            attendee=attendee11
        )

        event12 = Event(
            title='Digital Transformation Conference',
            logo='logo12.jpg',
            name='Digital Transformation Conference',
            location='Sarit Centre',
            period='20th March, 2025 - 22nd March, 2025',
            event_description='Learn how digital technologies are reshaping businesses and industries.',
            organizer=organizer1,
            attendee=attendee12
        )

        event13 = Event(
            title='Blockchain Innovation Forum',
            logo='logo13.jpg',
            name='Blockchain Innovation Forum',
            location='Nairobi',
            period='10th April, 2025 - 12th April, 2025',
            event_description='Discover the latest innovations and trends in blockchain technology.',
            organizer=organizer2,
            attendee=attendee13
        )

        event14 = Event(
            title='Cybersecurity Summit',
            logo='logo14.jpg',
            name='Cybersecurity Summit',
            location='Nairobi',
            period='15th May, 2025 - 17th May, 2025',
            event_description='Address the challenges and opportunities in cybersecurity.',
            organizer=organizer3,
            attendee=attendee14
        )

        event15 = Event(
            title='Data Science Conference',
            logo='logo15.jpg',
            name='Data Science Conference',
            location='Nairobi',
            period='20th June, 2025 - 22nd June, 2025',
            event_description='Explore the latest trends and techniques in data science.',
            organizer=organizer1,
            attendee=attendee15
        )

        event16 = Event(
            title='Mobile App Development Summit',
            logo='logo16.jpg',
            name='Mobile App Development Summit',
            location='Nairobi',
            period='10th July, 2025 - 12th July, 2025',
            event_description='Learn about the latest tools and frameworks for mobile app development.',
            organizer=organizer2,
            attendee=attendee16
        )

        event17 = Event(
            title='Cloud Computing Conference',
            logo='logo17.jpg',
            name='Cloud Computing Conference',
            location='Nairobi',
            period='15th August, 2025 - 17th August, 2025',
            event_description='Discover the benefits and challenges of cloud computing technologies.',
            organizer=organizer3,
            attendee=attendee17
        )

        event18 = Event(
            title='Fintech Expo',
            logo='logo18.jpg',
            name='Fintech Expo',
            location='Nairobi',
            period='20th September, 2025 - 22nd September, 2025',
            event_description='Explore the latest innovations and disruptions in fintech industry.',
            organizer=organizer1,
            attendee=attendee18
        )

        event19 = Event(
            title='E-commerce Summit',
            logo='logo19.jpg',
            name='E-commerce Summit',
            location='Nairobi',
            period='10th October, 2025 - 12th October, 2025',
            event_description='Discover strategies for scaling and growing your e-commerce business.',
            organizer=organizer2,
            attendee=attendee19
        )

        event20 = Event(
            title='Artificial Intelligence Workshop',
            logo='logo20.jpg',
            name='AI Workshop',
            location='Nairobi',
            period='15th November, 2025 - 17th November, 2025',
            event_description='Hands-on workshop to explore AI concepts and applications.',
            organizer=organizer3,
            attendee=attendee20
        )



        
        # Create instances of reviews
        review1 = Review(
            score=4,
            comment="The Tech Summit was an enlightening experience. The speakers were knowledgeable and engaging, covering a wide range of topics in the tech industry. I particularly enjoyed the hands-on workshops, which provided valuable insights and practical skills. Overall, it was a great event, and I look forward to attending more in the future.",
            event=event1,
            attendee=attendee1
        )

        review2 = Review(
            score=2,
            comment="Attending the Cancer Summit was a truly eye-opening experience. The speakers were experts in their fields, and their presentations were both informative and inspiring. The event provided a comprehensive overview of the latest advancements in cancer research, treatment, and prevention strategies. I left feeling empowered and motivated to make a difference in the fight against cancer.",
            event=event2,
            attendee=attendee2
        )

        review3 = Review(
            score=5,
            comment="I had the pleasure of attending the Artificial Intelligence Summit, and I must say, it exceeded my expectations. The sessions were well-organized, covering a diverse range of AI applications and technologies. The networking opportunities were also fantastic, allowing me to connect with industry professionals and fellow enthusiasts. Overall, it was a valuable learning experience that I would highly recommend.",
            event=event3,
            attendee=attendee3
        )

        review4 = Review(
            score=3,
            comment="The Digital Transformation Conference was an excellent event that provided valuable insights into the digital landscape. The keynote speakers were engaging, and the panel discussions were thought-provoking. I particularly enjoyed the interactive workshops, where I had the opportunity to collaborate with industry experts and explore practical strategies for digital transformation. Overall, it was a highly informative and inspiring conference.",
            event=event4,
            attendee=attendee4
        )

        review5 = Review(
            score=3,
            comment="Attending the Blockchain Innovation Forum was a game-changer for me. The event provided a comprehensive overview of blockchain technology and its potential applications across various industries. The speakers were experts in their fields, and their presentations were both informative and engaging. I left the forum with a deeper understanding of blockchain and a newfound excitement for its future possibilities.",
            event=event5,
            attendee=attendee5
        )

        review6 = Review(
            score=5,
            comment="The Cybersecurity Summit was an insightful event that shed light on the latest trends and challenges in cybersecurity. The speakers were knowledgeable, and their presentations were informative. I particularly enjoyed the discussions on emerging threats and cybersecurity best practices. The summit provided valuable insights that will help me enhance my organization's security posture.",
            event=event6,
            attendee=attendee6
        )

        review7 = Review(
            score=3,
            comment="I recently attended the Data Science Conference, and I must say, it was a fantastic learning experience. The sessions covered a wide range of topics, from machine learning algorithms to big data analytics. The speakers were experts in their fields, and their presentations were engaging and informative. I left the conference feeling inspired and equipped with new tools and techniques to apply in my data science projects.",
            event=event7,
            attendee=attendee7
        )

        review8 = Review(
            score=5,
            comment="The Mobile App Development Summit was an invaluable experience for anyone interested in app development. The sessions were well-structured, covering everything from UI/UX design to backend development. The hands-on workshops were particularly helpful, providing practical insights and tips for building high-quality mobile apps. I would highly recommend this summit to anyone looking to enhance their mobile app development skills.",
            event=event8,
            attendee=attendee8
        )

        review9 = Review(
            score=3,
            comment="Attending the Cloud Computing Conference was a transformative experience for me. The sessions were informative, covering a wide range of topics related to cloud computing, including infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS). The speakers were knowledgeable, and their presentations were engaging. Overall, it was a valuable learning opportunity that has expanded my understanding of cloud technologies.",
            event=event9,
            attendee=attendee9
        )

        review10 = Review(
            score=5,
            comment="The Fintech Expo exceeded my expectations in every way. The event brought together fintech experts, innovators, and thought leaders from around the world to discuss the latest trends and developments in the fintech industry. The keynote presentations were insightful, and the panel discussions provided valuable insights into the future of finance. I left the expo feeling inspired and excited about the possibilities of fintech.",
            event=event10,
            attendee=attendee10
        )
        review11 = Review(
            score=4,
            comment="The HealthTech Summit was an enlightening event that showcased the latest innovations and technologies in healthcare. The presentations were informative and thought-provoking, covering topics such as telemedicine, digital health, and wearable devices. I particularly enjoyed the interactive demos, which allowed attendees to experience firsthand how technology is transforming the healthcare industry. Overall, it was a valuable opportunity to learn from leading experts and gain insights into the future of healthcare.",
            event=event11,
            attendee=attendee11
        )

        review12 = Review(
            score=2,
            comment="Attending the Renewable Energy Summit was a truly inspiring experience. The speakers were passionate about sustainability and shared valuable insights into the latest advancements in renewable energy technologies. From solar power to wind energy, the summit covered a wide range of topics, providing attendees with actionable strategies for promoting a cleaner, greener future. I left the summit feeling empowered and motivated to advocate for renewable energy solutions in my community.",
            event=event12,
            attendee=attendee12
        )

        review13 = Review(
            score=2,
            comment="The E-commerce Expo was a fantastic event for anyone involved in e-commerce. The sessions were informative and practical, covering topics such as online marketing, customer experience, and logistics. I particularly enjoyed the case studies, which provided real-world examples of successful e-commerce strategies. The expo provided valuable insights that will help me optimize my online store and attract more customers.",
            event=event13,
            attendee=attendee13
        )

        review14 = Review(
            score=3,
            comment="Attending the AgriTech Conference was a transformative experience for me. The presentations were eye-opening, covering a wide range of topics related to agricultural technology and innovation. From precision farming to smart irrigation systems, the conference showcased the latest advancements in AgriTech and their potential to revolutionize the agricultural industry. I left the conference feeling inspired and excited about the future of farming.",
            event=event14,
            attendee=attendee14
        )

        review15 = Review(
            score=5,
            comment="The Future of Work Symposium was an insightful event that explored the evolving landscape of work in the digital age. The speakers were experts in their fields, and their presentations were both informative and thought-provoking. From remote work to automation, the symposium covered a wide range of topics, providing valuable insights into the future of work. I left the event with a deeper understanding of the challenges and opportunities that lie ahead.",
            event=event15,
            attendee=attendee15
        )

        review16 = Review(
            score=4,
            comment="Attending the Smart Cities Summit was an enlightening experience that showcased the latest innovations in urban planning and development. The presentations were informative and engaging, covering topics such as sustainable transportation, smart infrastructure, and digital governance. I particularly enjoyed the case studies, which highlighted successful smart city initiatives from around the world. The summit provided valuable insights into how technology can improve the quality of life in cities.",
            event=event16,
            attendee=attendee16
        )

        review17 = Review(
            score=3,
            comment="The EdTech Expo was a fantastic event for anyone interested in educational technology. The sessions were informative and practical, covering topics such as online learning platforms, virtual classrooms, and adaptive learning tools. I particularly enjoyed the hands-on demos, which allowed attendees to explore the latest EdTech solutions firsthand. The expo provided valuable insights that will help me enhance my teaching practices and support student learning.",
            event=event17,
            attendee=attendee17
        )

        review18 = Review(
            score=3,
            comment="Attending the Robotics Conference was a truly inspiring experience. The presentations were engaging, covering a wide range of topics related to robotics and artificial intelligence. From autonomous drones to humanoid robots, the conference showcased the latest advancements in robotics technology and their potential applications across various industries. I left the conference feeling excited about the future of robotics and motivated to explore new opportunities in this rapidly evolving field.",
            event=event18,
            attendee=attendee18
        )

        review19 = Review(
            score=5,
            comment="The Space Exploration Symposium was a fascinating event that explored the frontiers of space exploration. The presentations were informative and thought-provoking, covering topics such as interplanetary travel, space habitats, and extraterrestrial colonization. I particularly enjoyed the panel discussions, which provided insights into the challenges and opportunities of space exploration. The symposium sparked my curiosity about the cosmos and left me eager to learn more.",
            event=event19,
            attendee=attendee19
        )

        review20 = Review(
            score=4,
            comment="The Gaming Industry Summit was a fantastic event for anyone passionate about gaming. The sessions were informative and engaging, covering topics such as game design, virtual reality, and esports. I particularly enjoyed the keynote presentations, which provided insights into the latest trends and developments in the gaming industry. The summit provided valuable insights that will help me stay informed and inspired as I pursue a career in game development.",
            event=event20,
            attendee=attendee20
        )


        # Add instances to the session
        db.session.add_all([organizer1, organizer2, organizer3, organizer4, organizer5,
                    organizer6, organizer7, organizer8, organizer9, organizer10,
                    organizer11, organizer12, organizer13, organizer14, organizer15,
                    organizer16, organizer17, organizer18, organizer19, organizer20,
                    attendee1, attendee2, attendee3, attendee4, attendee5,
                    attendee6, attendee7, attendee8, attendee9, attendee10,
                    attendee11, attendee12, attendee13, attendee14, attendee15,
                    attendee16, attendee17, attendee18, attendee19, attendee20,
                    event1, event2, event3, event4, event5,
                    event6, event7, event8, event9, event10,
                    event11, event12, event13, event14, event15,
                    event16, event17, event18, event19, event20,
                    review1, review2, review3, review4, review5,
                    review6, review7, review8, review9, review10,
                    review11, review12, review13, review14, review15,
                    review16, review17, review18, review19, review20])


        # Commit the changes
        db.session.commit()

    seed()
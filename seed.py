from models import User,Post,Tag,PostTag, db
from app import app


with app.app_context():
    # drop and create table's info
    db.drop_all()
    db.create_all()

    # if table is not empty it then it will empty
    User.query.delete()

    # Test Users 
    whis = User(first_name='Whis',last_name='Dogman')
    vamp = User(first_name='Vamp',last_name='Dogman')
    tiggy = User(first_name='Tiggy',last_name='Tigerson', image_url='https://w0.peakpx.com/wallpaper/1002/951/HD-wallpaper-jujutsu-kaisen-op-strong-anime-gojo-satoru-love.jpg')

    # add test Users
    db.session.add_all([whis,vamp,tiggy])
    # commit test User
    db.session.commit()

    # Test Posts
    post1 = Post(title = "fun",content = "dwaha0dwjowajd" , user_id = 1)
    post2 = Post(title = "kng queen",content = "njsnefoanfa" , user_id = 1)
    post3 = Post(title = "Meowers",content = "dwaoijnwodnjaojoawijowajawd" , user_id = 2)
    post4 = Post(title = "Dad",content = "d" , user_id = 3)

    # add test Posts
    db.session.add_all([post1,post2,post3,post4])
    # commit test Posts
    db.session.commit()

    # Test Tags
    tag1 = Tag(name='fun')
    tag2 = Tag(name='mongo')
    tag3 = Tag(name='sad')

    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()

    # Test PostTage 

    posttag1 = PostTag(post_id = 1 , tag_id = 1)
    posttag2 = PostTag(post_id = 3 , tag_id = 2)
    posttag3 = PostTag(post_id = 4 , tag_id = 3)
    posttag4 = PostTag(post_id = 2 , tag_id = 1)

    db.session.add_all([posttag1,posttag2,posttag3,posttag4])
    db.session.commit()


    print("Database seeded!")

    print(Tag.query.all())
import os
from instagrapi import Client
from PIL import Image

# List of captions
captions = [
    "Let AI handle your IG hustle ☕📱 Your daily content—done. #AIContent #InstaAutomation #EntrepreneurLife #SocialMediaHacks",
    "Your content, on schedule.Set it once. Let it flow daily. 🚀#AutomatedPosting #DigitalFlow #EffortlessContent #AIinAction",
    "You choose your role. We’ll handle the content. #ContentAsAService #StartupTools #AutomateYourLife",
    "Create. Schedule. Repeat. Your brand deserves this upgrade. #DigitalWorkflow #FuturisticMarketing #AIContentCreation",
    "Timely. Trendy. Tailored. One post a day keeps the silence away. #InstaGrowth #DailyPosts #AIAgency",
    "Sleep mode: ON. Stress mode: OFF. We’ve got your socials. #PassivePosting #SmartMarketing #SleepAndScale",
    "AI meets aesthetics. We post. You profit. #AIArt #InstagramManager #DigitalCreatives",
    "What if your calendar filled itself? Now it can. #AutomatedContent #SocialMediaSolutions #ContentPlanning",
    "When your content's on autopilot, results follow. #BusinessGrowth #AIinBusiness #ContentSuccess",
    "Pick your content weapon. Daily. Doubled. Tripled. #SocialPlans #InstagramService #AIPlans",
    "Launch your brand into orbit—one post at a time. #StartupFuel #InstagramGrowth #LaunchWithAI",
    "Your IG gift? Stress-free content. #DoneForYou #InstaGift #CreatorSupport",
    "Content that never stops. We keep it moving. #ContentMachine #AlwaysOn #SocialMediaEngine",
    "We don’t just post. We post what works. #SmartPosting #TrendDetection #AIInsights",
    "Brains meet branding. Let AI power your Insta. #AIThinking #InstaUpgrade #DigitalBrain"
]

# Folder containing images
folder_path = "generated_images_ai_pr"

# Instagram credentials
username = "gear_services"
password = "utils@321"

# Initialize the Instagram client
cl = Client()

# Login to Instagram
try:
    cl.login(username, password)
except Exception as e:
    print(f"Login failed: {e}")
    exit()

# Get the list of images in the folder
images = sorted(os.listdir(folder_path))

if not images:
    print("No images found in the folder.")
    exit()

# Select the first image and corresponding caption
image_name = images[0]
image_path = os.path.join(folder_path, image_name)
caption_index = int(image_name.split('post')[1].split('.')[0]) - 1  # Extract index from filename
caption = captions[caption_index] if caption_index < len(captions) else "Default caption"

# Ensure the image meets Instagram's requirements
try:
    image = Image.open(image_path)
    image = image.convert("RGB")
    image.thumbnail((1080, 1080), Image.LANCZOS)
    processed_image_path = os.path.join(folder_path, "processed_image.jpg")
    image.save(processed_image_path, "JPEG")
except Exception as e:
    print(f"Image processing failed: {e}")
    exit()

# Upload the image
try:
    media = cl.photo_upload(processed_image_path, caption)
    print(f"Image uploaded successfully: {media.dict().get('code')}")
    # Delete the original image after successful upload
    os.remove(image_path)
    print(f"Deleted image: {image_name}")
except Exception as e:
    print(f"Image upload failed: {e}")
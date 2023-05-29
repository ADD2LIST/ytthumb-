import streamlit as st

import requests

def save_image(url):

    response = requests.get(url)

    if response.status_code == 200:

        return response.content

    return None

def main():

    st.title("YouTube Thumbnail Downloader")

    video_input = st.text_input("Enter YouTube video URL or video ID")

    if st.button("Download Thumbnail"):

        try:

            thumbnail_url = f"https://img.youtube.com/vi/{video_input}/maxresdefault.jpg"

            image_data = save_image(thumbnail_url)

            if image_data is not None:

                st.image(image_data, use_column_width=True, caption='Thumbnail')

                download_link = f'<a href="{thumbnail_url}" download="thumbnail.jpg">Download Thumbnail</a>'

                st.markdown(download_link, unsafe_allow_html=True)

            else:

                st.warning("Thumbnail not found for the given input.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    main()



                

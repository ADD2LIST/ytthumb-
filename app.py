import streamlit as st

import ytthumb

import requests

from io import BytesIO

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

            if "|" in video_input:

                video_id, default_quality = video_input.split("|", 1)

            else:

                video_id = video_input

                default_quality = "sd"

            thumbnail_urls = ytthumb.get_thumbnail_urls(video_id)

            if thumbnail_urls:

                st.markdown("### Thumbnail Qualities:")

                for quality, url in thumbnail_urls.items():

                    if quality == default_quality:

                        st.markdown(f"- **{quality}**: [Download]({url}) (default)")

                    else:

                        st.markdown(f"- **{quality}**: [Download]({url})")

                image_data = save_image(thumbnail_urls[default_quality])

                if image_data is not None:

                    st.image(image_data, use_column_width=True, caption='Thumbnail')

            else:

                st.warning("Thumbnail not found for the given input.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    main()

import streamlit as st

import ytthumb

def main():

    st.title("YouTube Thumbnail Downloader")

    video_input = st.text_input("Enter YouTube video URL or video ID")

    if st.button("Download Thumbnail"):

        try:

            if "|" in video_input:

                video_id, quality = video_input.split("|", 1)

            else:

                video_id = video_input

                quality = "sd"

            thumbnail_url = ytthumb.thumbnail(video_id, quality)

            if thumbnail_url:

                st.image(thumbnail_url, use_column_width=True)

            else:

                st.warning("Thumbnail not found for the given input.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":

    main()


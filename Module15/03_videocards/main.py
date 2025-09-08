quantity = int(input('Количество видеокарт: '))
video_card_list, video_card_list_new, max_name = [], [], 0

for video_card in range(quantity):
    print(video_card + 1, 'видеокарта:', end=' ')
    video_name = int(input(''))
    video_card_list.append(video_name)
    if video_name > max_name:
        max_name = video_name

for video_c in video_card_list:
    if video_c != max_name:
        video_card_list_new.append(video_c)

print('\nСтарый список видеокарт:', video_card_list)
print('Новый список видеокарт:', video_card_list_new)

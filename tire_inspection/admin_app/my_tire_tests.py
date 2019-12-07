import cv2

class tire_tests:
	def ink_test(filename):
		frame = cv2.imread(filename)
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		_, thresh = cv2.threshold(gray,150,200,0)
		img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		def big_contour():
			big = cv2.contourArea(contours[0])
			for contour in contours:
				area = cv2.contourArea(contour)
				print(area)
				if (area>big):
					big = area
			return big
		def count_contour():
			count = 0
			for contour in contours:
				count = count + 1
			return count
		cv2.fillPoly(frame,pts=[contours[17]],color=(0,0,0))
		cv2.fillPoly(frame,pts=[contours[34]],color=(0,0,0))
		cv2.fillPoly(frame,pts=[contours[44]],color=(0,0,0))
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		_, thresh = cv2.threshold(gray,165,165,0)
		img, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(frame,contours,-1,(0,255,0),3)
		count = 0
		for contour in contours:
			count = count + 1
		if count > 0:
			flag = 1
		else:
			flag = 0
		if flag == 1:
			print('defective')
		else:
			print('non-defective')
		cv2.imshow('frame',frame)
		cv2.imshow('gray',gray)
		cv2.imshow('thresh',thresh)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
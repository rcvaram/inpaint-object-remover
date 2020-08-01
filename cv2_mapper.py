  def cv2_wrapper(image_path,mask_path):
    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path)
    img = cv2.cvtColor(cv2.resize(img, (400, 300)),cv2.COLOR_BGR2RGB)
    inpainter = Inpainter(image=img, mask=mask,plot_progress=True)
    dst =cv2.cvtColor(inp.inpaint(),cv2.COLOR_RGB2BGR)
    return dst

  

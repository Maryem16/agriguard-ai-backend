def recommend_practices(carbon):
  if carbon < 2:
      return ["Switch to no-till", "Add organic compost", "Plant cover crops"]
  else:
      return ["Maintain current practice", "Monitor soil moisture"]